from sqlalchemy import create_engine, inspect
import pandas as pd
from app.config import settings

engine = create_engine(settings.MYSQL_URI)

def fetch_all_mysql_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    data = {}
    for table in tables:
        df = pd.read_sql_table(table, engine)
        data[table] = df
    return data
