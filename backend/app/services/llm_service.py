#  app/services/llm_service.py
import openai
from app.config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_llm_reply(history: list[dict], new_message: str) -> str:
    messages = history + [{"role": "user", "content": new_message}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']
