from decimal import Decimal

if __package__ and __package__.startswith("app."):
    from ..models.incident import PaymentIncident
    from ..repositories.incident_repository import IncidentRepository
else:
    from models.incident import PaymentIncident
    from repositories.incident_repository import IncidentRepository


class IncidentService:

    VALID_STATUSES = {"NEW", "FAILED", "SUCCESS", "RESOLVED"}

    def __init__(self):
        self.repository = IncidentRepository()

    def create_incident(self, incident: PaymentIncident):

        # Validate payment status
        if incident.status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid payment status: {incident.status}"
            )

        # Validate payment amount
        if incident.amount <= Decimal("0"):
            raise ValueError("Payment amount must be positive")

        # Save incident
        return self.repository.save(incident)

    def get_incident(self, incident_id: int):

        incident = self.repository.find_by_id(incident_id)

        if incident is None:
            raise ValueError(
                f"Incident {incident_id} not found"
            )

        return incident

    def get_failed_incidents(self):

        return self.repository.find_by_status("FAILED")

    def get_incident_summary(self):

        incidents = self.repository.find_all()

        total = len(incidents)

        failed = sum(
            1 for incident in incidents
            if incident.status == "FAILED"
        )

        successful = sum(
            1 for incident in incidents
            if incident.status == "SUCCESS"
        )

        return {
            "total_incidents": total,
            "failed_incidents": failed,
            "successful_incidents": successful
        }