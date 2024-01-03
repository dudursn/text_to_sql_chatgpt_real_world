from langchain.chat_models import ChatOpenAI
import openai
import os

def get_llm(temperature=0, max_tokens=50, n=1):
    apikey = os.environ["OPENAI_API_KEY"]
    openai.api_key = apikey
    return ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo", max_tokens=max_tokens, n=n)