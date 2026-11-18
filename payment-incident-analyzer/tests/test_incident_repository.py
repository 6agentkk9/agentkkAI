from decimal import Decimal

from payment_analyzer.models.incident import PaymentIncident
from payment_analyzer.repositories.incident_repository import IncidentRepository


def test_repository_save_and_find(tmp_path):
    repository = IncidentRepository(tmp_path / "test.db")
    repository.create_tables()

    incident = PaymentIncident(
        payment_id="PAY-123",
        amount=Decimal("45.67"),
        currency="USD",
        status="FAILED",
        error_code="51",
    )

    saved = repository.save(incident)
    found = repository.find_by_id(saved.incident_id)

    assert found is not None
    assert found.payment_id == "PAY-123"
    assert found.amount == Decimal("45.67")
