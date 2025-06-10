# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat
from app.routers import office
from app.routers import search

app = FastAPI()

# ✅ Allow frontend (e.g., http://localhost:3000)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(office.router, prefix="/api/office", tags=["Office DB"])
app.include_router(search.router, prefix="/api/search")
