# backend/app/services/llm_service.py
import cohere
from app.config import settings

co = cohere.Client(settings.COHERE_API_KEY)

def generate_llm_reply(history: list[dict], new_message: str) -> str:
    # Convert to cohere's format
    cohere_messages = [
        {"role": msg["role"], "message": msg["content"]} for msg in history
    ]
    cohere_messages.append({"role": "USER", "message": new_message})

    response = co.chat(
        model="command-r",  # Or "command-r-plus" if allowed
        message=new_message,
        chat_history=cohere_messages[:-1],  # only previous history
        temperature=0.7,
        max_tokens=300
    )

    return response.text.strip()
