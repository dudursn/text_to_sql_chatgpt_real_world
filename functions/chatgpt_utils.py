import time
import openai
import os

# ----------------------------------------------
def get_openai_response(prompt, user_input, temperature=0, max_tokens=50, delay=None):
    apikey = os.environ["OPENAI_API_KEY"]
    openai.api_key = apikey
    msgs = [{"role": "system", "content": prompt},
            {"role": "user", "content": user_input}]
    return get_openai_response_msg(msgs, temperature, max_tokens, delay)


def get_openai_response_msg(messages = [{"role": "system", "content": "You are a helpful assistant."}], temperature=0, max_tokens=50, delay=None, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    if delay is not None:
        # Sleep for the delay
        time.sleep(delay)

    message = response.choices[0].message
    message["usage"] = response.usage
    return message

def get_openai_function_call(messages = [{"role": "system", "content": "You are a helpful assistant."}],
                             functions=[],
                             function_call="auto",
                             temperature=0,
                             max_tokens=50,
                             delay=None,
                             model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        functions=functions,
        function_call=function_call
    )
    if delay is not None:
        # Sleep for the delay
        time.sleep(delay)
    
    message = response.choices[0].message
    message["usage"] = response.usage
    return message

def get_embeddings(text, model="text-embedding-ada-002"):
    response = openai.Embedding.create(
        input=text,
        model=model
    )
    return response.data[0].embedding