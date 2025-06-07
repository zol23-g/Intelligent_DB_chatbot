# app/models/chat.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, default="1")
    message = Column(Text)  # User's message
    response = Column(Text)  # Assistant's response
    timestamp = Column(DateTime, default=datetime.utcnow)
