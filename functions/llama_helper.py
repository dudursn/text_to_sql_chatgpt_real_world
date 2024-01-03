import json
from typing import List, Literal, TypedDict
import requests
import time

Role = Literal["user", "assistant"]

class Message(TypedDict):
    role: Role
    content: str

Dialog = List[Message]

B_INST, E_INST = "<s>[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
def format_prompt(dialogs):
    prompts = []
    for dialog in dialogs:
        if dialog[0]["role"] == "system":
            dialog = [
            {
                "role": dialog[1]["role"],
                "content": B_SYS
                + dialog[0]["content"]
                + E_SYS
                + dialog[1]["content"],
            }
        ] + dialog[2:]
            
        assert all([msg["role"] == "user" for msg in dialog[::2]]) and all(
            [msg["role"] == "assistant" for msg in dialog[1::2]]
        ), (
            "model only supports 'system','user' and 'assistant' roles, "
            "starting with user and alternating (u/a/u/a/u...)"
        )
        
        """
        Please verify that your tokenizer support adding "[INST]", "[/INST]" to your inputs.
        Here, we are adding it manually.
        """
        prompt_final = ""
        for prompt, answer in zip(dialog[::2], dialog[1::2]):
            prompt_final += f"{B_INST} {(prompt['content']).strip()} {E_INST} {(answer['content']).strip()} "
           
        assert (
            dialog[-1]["role"] == "user"
        ), f"Last message must be from user, got {dialog[-1]['role']}"

        prompt_final += f"{B_INST} {(dialog[-1]['content']).strip()} {E_INST}"
        prompts.append(prompt_final)
        
    return prompts

class LlamaHelper:
    def __init__(self, api_url, system_prompt=None):
        self.api_url = api_url

        self.generation_endpoint = f"{api_url}/generate/"
        self.task_endpoint = f"{api_url}/task/"

        if system_prompt is None:
            self.system_prompt = "Você é um assistente prestativo e educado. Seu trabalho é ajudar o usuário da melhor forma possível. Seja breve e direto e não use emojis."
        else:
            self.system_prompt = system_prompt

    def create_generation_request(self, user_message, history=[]):

        """
        Todo: history
        if history is empty, add system prompt, else don't
        append user message to history
        """

        messages = [[{"role": "system", "content": self.system_prompt},
                     {"role": "user", "content": user_message}]]
        prompt = format_prompt(messages)[0]
        params = {
            "prompt": prompt,
            "temperature": 0.3,
            "max_new_tokens": 4096,
        }
        response = requests.post(self.generation_endpoint, json=params)
        return response.json()["task_id"]
    
    def get_task_result(self, task_id):
        params = {
            "task_id": task_id
        }
        response = requests.post(self.task_endpoint, json=params)
        if "status" in response.json():
            if response.json()["status"] == "Task not completed yet":
                return False
        try:
            result = response.json()["result"][0]["generated_text"].split("[/INST]")[-1]
            return result
        except:
            print("Error isolating model output.")
            result = response.json()["result"][0]["generated_text"]

    def generate_response(self, user_message, interval=0.5, timeout=300):
        task_id = self.create_generation_request(user_message)
        
        start = time.time()
        while time.time() - start < timeout:
            result = self.get_task_result(task_id)
            if result:
                return result
        
        print("Timeout")
        return False