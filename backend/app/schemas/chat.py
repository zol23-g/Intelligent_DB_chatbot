# app/schemas/chat.py
from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    message: str
    user_id: str = "1"  # Default to "1"

class ChatResponse(BaseModel):
    reply: str
    timestamp: datetime