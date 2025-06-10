# app/services/office_data_service.py
from sqlalchemy import text
from app.db.session import OfficeSessionLocal

def test_office_db_connection():
    try:
        with OfficeSessionLocal() as session:
            result = session.execute(text("SELECT * FROM accounts_account LIMIT 2")).mappings().fetchone()

            if not result:
                return ["No data found in accounts_account table."]

            # Convert result into a list of readable key-value strings
            facts = [f"{key}: {value}" for key, value in result.items()]
            return facts

    except Exception as e:
        return [f"Error fetching data: {str(e)}"]

