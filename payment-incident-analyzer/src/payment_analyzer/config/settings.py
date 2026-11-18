import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Read application settings from environment variables."""

    def __init__(self) -> None:
        self.database_path = Path(
            os.getenv("PAYMENT_ANALYZER_DB_PATH", "data/payment_incidents.db")
        )
        self.payment_api_base_url = os.getenv(
            "PAYMENT_API_BASE_URL", "http://localhost:8000"
        ).rstrip("/")
        self.payment_api_timeout_seconds = float(
            os.getenv("PAYMENT_API_TIMEOUT_SECONDS", "10")
        )
        self.log_level = os.getenv("LOG_LEVEL", "INFO").upper()


settings = Settings()
