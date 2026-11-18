from decimal import Decimal

from payment_analyzer.models.incident import PaymentIncident
from payment_analyzer.services.incident_service import IncidentService


class FakeRepository:
    def __init__(self):
        self.saved = []

    def save(self, incident):
        self.saved.append(incident)
        return incident.model_copy(update={"incident_id": 1})

    def find_by_id(self, incident_id):
        return None

    def find_all(self):
        return list(self.saved)


def test_service_injects_repository_and_saves():
    repository = FakeRepository()
    service = IncidentService(repository)
    incident = PaymentIncident(
        payment_id="PAY-9",
        amount=Decimal("10.00"),
        currency="USD",
        status="FAILED",
    )

    result = service.create_incident(incident)

    assert result.incident_id == 1
    assert len(repository.saved) == 1
