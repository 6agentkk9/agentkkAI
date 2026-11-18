import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from payment_analyzer.models.incident import PaymentIncident


class IncidentRepository:
    """SQLite repository for payment incidents."""

    def __init__(self, db_path: str | Path = "data/payment_incidents.db") -> None:
        self.db_path = Path(db_path)

    @contextmanager
    def _connection(self) -> Iterator[sqlite3.Connection]:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def create_tables(self) -> None:
        with self._connection() as connection:
            connection.execute(
                """
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
                """
            )

    def save(self, incident: PaymentIncident) -> PaymentIncident:
        with self._connection() as connection:
            if incident.incident_id is None:
                cursor = connection.execute(
                    """
                    INSERT INTO payment_incidents
                    (payment_id, amount, currency, status, error_code,
                     error_description, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        incident.payment_id,
                        str(incident.amount),
                        incident.currency,
                        incident.status,
                        incident.error_code,
                        incident.error_description,
                        incident.created_at.isoformat(),
                    ),
                )
                incident_id = cursor.lastrowid
            else:
                connection.execute(
                    """
                    INSERT OR REPLACE INTO payment_incidents
                    (incident_id, payment_id, amount, currency, status,
                     error_code, error_description, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        incident.incident_id,
                        incident.payment_id,
                        str(incident.amount),
                        incident.currency,
                        incident.status,
                        incident.error_code,
                        incident.error_description,
                        incident.created_at.isoformat(),
                    ),
                )
                incident_id = incident.incident_id

        return incident.model_copy(update={"incident_id": incident_id})

    def find_by_id(self, incident_id: int) -> PaymentIncident | None:
        with self._connection() as connection:
            row = connection.execute(
                "SELECT * FROM payment_incidents WHERE incident_id = ?",
                (incident_id,),
            ).fetchone()
        return self._to_model(row) if row else None

    def find_all(self) -> list[PaymentIncident]:
        with self._connection() as connection:
            rows = connection.execute(
                "SELECT * FROM payment_incidents ORDER BY incident_id"
            ).fetchall()
        return [self._to_model(row) for row in rows]

    def find_by_status(self, status: str) -> list[PaymentIncident]:
        with self._connection() as connection:
            rows = connection.execute(
                "SELECT * FROM payment_incidents WHERE status = ? ORDER BY incident_id",
                (status.upper(),),
            ).fetchall()
        return [self._to_model(row) for row in rows]

    @staticmethod
    def _to_model(row: sqlite3.Row) -> PaymentIncident:
        return PaymentIncident(
            incident_id=row["incident_id"],
            payment_id=row["payment_id"],
            amount=row["amount"],
            currency=row["currency"],
            status=row["status"],
            error_code=row["error_code"],
            error_description=row["error_description"],
            created_at=row["created_at"],
        )
