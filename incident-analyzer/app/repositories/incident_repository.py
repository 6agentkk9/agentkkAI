from decimal import Decimal
from datetime import datetime
from webbrowser import get

if __package__ and __package__.startswith("app."):
    from ..database import get_connection
    from ..models.incident import PaymentIncident
else:
    from database import get_connection
    from models.incident import PaymentIncident


class IncidentRepository:

    def __init__(self, db_path=None):
        self.db_path = db_path

    def save(self, incident: PaymentIncident):

        with get_connection(self.db_path) as connection:
            cursor = connection.execute("""
                INSERT INTO payment_incidents (
                    payment_id,
                    amount,
                    currency,
                    status,
                    error_code,
                    error_description,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                incident.payment_id,
                str(incident.amount),
                incident.currency,
                incident.status,
                incident.error_code,
                incident.error_description,
                incident.created_at.isoformat()
            ))

            incident.incident_id = cursor.lastrowid

        return incident

    def find_by_id(self, incident_id: int):

        with get_connection(self.db_path) as connection:
            row = connection.execute("""
                SELECT *
                FROM payment_incidents
                WHERE incident_id = ?
            """, (incident_id,)).fetchone()

        if row is None:
            return None

        return self._map_to_model(row)

    def find_all(self):

        with get_connection(self.db_path) as connection:
            rows = connection.execute("""
                SELECT *
                FROM payment_incidents
                ORDER BY incident_id
            """).fetchall()

        return [self._map_to_model(row) for row in rows]

    def find_by_status(self, status: str):

        with get_connection(self.db_path) as connection:
            rows = connection.execute("""
                SELECT *
                FROM payment_incidents
                WHERE status = ?
                ORDER BY incident_id
            """, (status,)).fetchall()

        return [self._map_to_model(row) for row in rows]

    def find_by_error_code(self, error_code: str):

        with get_connection() as connection:
            rows = connection.execute("""
                SELECT *
                FROM payment_incidents
                WHERE error_code = ?
                ORDER BY incident_id
            """, (error_code,)).fetchall()

        return [self._map_to_model(row) for row in rows]


    
    @staticmethod
    def _map_to_model(row):

        return PaymentIncident(
            incident_id=row["incident_id"],
            payment_id=row["payment_id"],
            amount=Decimal(row["amount"]),
            currency=row["currency"],
            status=row["status"],
            error_code=row["error_code"] or "",
            error_description=row["error_description"] or "",
            created_at=datetime.fromisoformat(row["created_at"])
        )