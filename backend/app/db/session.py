# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Chatbot DB
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Office DB
office_db_url = (
    f"postgresql://{settings.OFFICE_DB_USER}:{settings.OFFICE_DB_PASSWORD}"
    f"@{settings.OFFICE_DB_HOST}:{settings.OFFICE_DB_PORT}/{settings.OFFICE_DB_NAME}"
)
OfficeEngine = create_engine(office_db_url)
OfficeSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=OfficeEngine)
