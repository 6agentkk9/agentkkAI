import sqlite3
from pathlib import Path


# Default application database
DATABASE_PATH = Path("data/payment_incidents.db")


def get_connection(db_path=None):
    """
    Create and return a SQLite database connection.

    If db_path is provided, use that database.
    Otherwise, use the default application database.
    """

    path = Path(db_path) if db_path else DATABASE_PATH

    # Create the parent directory if it does not exist.
    path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(path)

    # Return rows that support column-name access.
    connection.row_factory = sqlite3.Row

    return connection


def create_tables(db_path=None):
    """
    Create application database tables if they do not exist.
    """

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