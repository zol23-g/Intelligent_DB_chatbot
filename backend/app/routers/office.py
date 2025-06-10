# app/routers/office.py
from fastapi import APIRouter
from app.services.office_data_test_service import test_office_db_connection

router = APIRouter(prefix="/office", tags=["Office DB"])

@router.get("/test-connection")
def test_connection():
    return test_office_db_connection()
