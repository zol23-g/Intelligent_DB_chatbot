# backend/app/main.py
from fastapi import FastAPI
from .routers import chat

app = FastAPI(
    title="Intelligent Chatbot API"
)

app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
