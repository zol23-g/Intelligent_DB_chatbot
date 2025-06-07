# app/services/db_service.py
from sqlalchemy.orm import Session
from app.models.chat import ChatMessage

def save_message(db: Session, user_id: str, role: str, message: str):
    chat = ChatMessage(user_id=user_id, role=role, message=message)
    db.add(chat)
    db.commit()

def get_chat_history(db: Session, user_id: str) -> list[dict]:
    chats = db.query(ChatMessage).filter(ChatMessage.user_id == user_id).order_by(ChatMessage.timestamp).all()
    return [{"role": c.role, "content": c.message} for c in chats]
