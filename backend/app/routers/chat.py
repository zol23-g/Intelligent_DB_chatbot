#  app/routers/chat.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.chat import ChatRequest, ChatResponse
from app.db.session import SessionLocal
from app.services.chat_service import handle_chat
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest, db: Session = Depends(get_db)):
    reply = handle_chat(db, payload.user_id, payload.message)
    return ChatResponse(reply=reply, timestamp=datetime.utcnow())

@router.get("/{user_id}", response_model=list[dict])
def get_chat_messages(user_id: str, db: Session = Depends(get_db)):
    from app.services.db_service import get_chat_history
    return get_chat_history(db, user_id)
