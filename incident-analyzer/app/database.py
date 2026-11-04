import sqlite3
from contextlib import contextmanager
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent / "data" / "payment_incidents.db"

@contextmanager
def get_connection(db_path=None):
    path = Path(db_path) if db_path else DATABASE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row

    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def create_tables(db_path=None):
    with get_connection(db_path) as connection:
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

    print("Database tables created successfully.")


if __name__ == "__main__":
    create_tables()