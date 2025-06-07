# backend/app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    COHERE_API_KEY = os.getenv("COHERE_API_KEY", "il5TNhrf0DPw17bURNZPOJdNs4XnVEnhwT8glPzX")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/DBchatbot")

settings = Settings()
