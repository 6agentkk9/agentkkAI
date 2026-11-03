import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent / "data" / "payment_incidents.db"


def get_connection():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    # Return query results as dictionary-like rows
    connection.row_factory = sqlite3.Row

    return connection


def create_tables():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS payment_incidents (
                incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
                payment_id TEXT NOT NULL,
                amount TEXT NOT NULL,
                currency TEXT NOT NULL,
                status TEXT NOT NULL,
                error_code TEXT,
                error_description TEXT,
                created_at TEXT NOT NULL
            )
        """)

    print("Database tables created successfully")


if __name__ == "__main__":
    create_tables()