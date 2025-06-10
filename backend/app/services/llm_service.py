# app/services/llm_service.py
import cohere
from app.config import settings
from app.services.office_data_test_service import test_office_db_connection
from app.services.semantic_search_service import query_semantic_elasticsearch  # You’ll define this

co = cohere.Client(settings.COHERE_API_KEY)

def generate_llm_reply(history: list[dict], new_message: str) -> str:
    role_map = {
        "user": "User",
        "assistant": "Chatbot",
        "system": "System"
    }

    # ===== 1. Fetch relevant facts from the office DB via semantic search =====
    try:
        semantic_facts = query_semantic_elasticsearch(new_message)
    except Exception as e:
        semantic_facts = [f"(Semantic search failed: {e})"]

    # # Optional: Fetch structured office data (fallback, or hybrid context)
    # try:
    #     office_facts = test_office_db_connection()
    # except Exception as e:
    #     office_facts = [f"(Office DB fetch failed: {e})"]

    # ===== 2. Combine context and describe the bot =====
    context_intro = (
        "You are an intelligent assistant trained to help users understand and explore data stored in an office database. "
        "Your responses should be based on the provided context. Use natural language to explain the answer clearly.\n\n"
        f"User Query: {new_message}\n\n"
        f"Context Data:\n"
    )

    context_data = "\n".join(semantic_facts or []) 
    system_prompt = context_intro + context_data

    print("=== LLM Context Data ===")
    print(system_prompt)
    print("========================")

    # ===== 3. Build the message payload =====
    cohere_messages = [{"role": "System", "message": system_prompt}] + [
        {"role": role_map.get(msg["role"].lower(), "User"), "message": msg["content"]}
        for msg in history
    ]

    print("=== Cohere Chat Prompt ===")
    for msg in cohere_messages:
        print(f"{msg['role']}: {msg['message']}")
    print("==========================")

    # ===== 4. Call Cohere Chat API =====
    response = co.chat(
        model="command-r-plus",
        message=new_message,
        chat_history=cohere_messages,
        temperature=0.7,
        max_tokens=300
    )

    print("=== Cohere Response ===")
    print(response.text.strip())
    print("========================")

    return response.text.strip()
