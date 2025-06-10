# backend/app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    COHERE_API_KEY = os.getenv("COHERE_API_KEY", "il5TNhrf0DPw17bURNZPOJdNs4XnVEnhwT8glPzX")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/DBchatbot")

    # Office DB
    OFFICE_DB_HOST = os.getenv("OFFICE_DB_HOST", "196.188.63.235")
    OFFICE_DB_PORT = os.getenv("OFFICE_DB_PORT", "5432")
    OFFICE_DB_NAME = os.getenv("OFFICE_DB_NAME", "hstoa_testdb")
    OFFICE_DB_USER = os.getenv("OFFICE_DB_USER", "hstoa")
    OFFICE_DB_PASSWORD = os.getenv("OFFICE_DB_PASSWORD", "password")

    MYSQL_URI = os.getenv("MYSQL_URI", "mysql+pymysql://root:@localhost/classicmodels")
    ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
    ELASTIC_USER = os.getenv("ELASTIC_USER", "elastic")
    ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD", "password")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

settings = Settings()
