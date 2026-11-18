from payment_analyzer.models.incident import PaymentIncident
from payment_analyzer.repositories.incident_repository import IncidentRepository


class IncidentService:
    """Business operations for payment incidents."""

    def __init__(self, repository: IncidentRepository) -> None:
        self.repository = repository

    def create_incident(self, incident: PaymentIncident) -> PaymentIncident:
        if incident.amount <= 0:
            raise ValueError("Incident amount must be positive")
        return self.repository.save(incident)

    def get_incident(self, incident_id: int) -> PaymentIncident | None:
        return self.repository.find_by_id(incident_id)

    def list_incidents(self) -> list[PaymentIncident]:
        return self.repository.find_all()
