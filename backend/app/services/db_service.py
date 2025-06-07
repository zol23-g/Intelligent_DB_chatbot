# app/services/db_service.py
from sqlalchemy.orm import Session
from app.models.chat import ChatMessage

def save_message(db: Session, user_input: str, assistant_response: str, user_id: str = "1"):
    chat = ChatMessage(
        user_id=user_id,
        message=user_input,
        response=assistant_response
    )
    db.add(chat)
    db.commit()

def get_chat_history(db: Session, user_id: str) -> list[dict]:
    chats = db.query(ChatMessage).filter(ChatMessage.user_id == user_id).order_by(ChatMessage.timestamp).all()
    
    history = []
    for c in chats:
        history.append({"role": "user", "content": c.message})
        history.append({"role": "assistant", "content": c.response})
    
    return history