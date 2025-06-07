# app/services/chat_service.py
from sqlalchemy.orm import Session
from app.services.db_service import get_chat_history, save_message
from app.services.llm_service import generate_llm_reply

def handle_chat(db: Session, user_id: str, user_input: str) -> str:
    history = get_chat_history(db, user_id)
    reply = generate_llm_reply(history, user_input)
    save_message(db, user_id, "user", user_input)
    save_message(db, user_id, "assistant", reply)
    return reply
