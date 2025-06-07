# backend/app/services/llm_service.py
import cohere
from app.config import settings

co = cohere.Client(settings.COHERE_API_KEY)

def generate_llm_reply(history: list[dict], new_message: str) -> str:
    role_map = {
        "user": "User",
        "assistant": "Chatbot",
        "system": "System"
    }

    # Format chat history for Cohere
    cohere_messages = [
        {"role": role_map.get(msg["role"].lower(), "User"), "message": msg["content"]}
        for msg in history
    ]

    # Log the prompt structure
    print("=== Cohere Prompt ===")
    for msg in cohere_messages:
        print(f"{msg['role']}: {msg['message']}")
    print(f"User: {new_message}")
    print("=====================")

    # Call Cohere
    response = co.chat(
        model="command-r",
        message=new_message,
        chat_history=cohere_messages,
        temperature=0.7,
        max_tokens=300
    )

    # Log the response
    print("=== Cohere Response ===")
    print(response.text.strip())
    print("========================")

    return response.text.strip()
