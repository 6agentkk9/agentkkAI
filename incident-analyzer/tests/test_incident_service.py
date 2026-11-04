from decimal import Decimal
from unittest.mock import Mock

import pytest

from app.models.incident import PaymentIncident
from app.services.incident_service import IncidentService

# rootdir: G:\agentkkAI run 
# python -m pytest -v .\incident-analyzer\tests

def test_create_incident():
    mock_repository = Mock()

    service = IncidentService(repository=mock_repository)

    incident = PaymentIncident(
        payment_id="PAY-10002",
        amount=Decimal("200.00"),
        currency="USD",
        status="FAILED",
        error_code="TO",
        error_description="Gateway timeout"
    )

    mock_repository.save.return_value = incident

    result = service.create_incident(incident)

    mock_repository.save.assert_called_once_with(incident)
    assert result.payment_id == "PAY-10002"


def test_reject_invalid_status():
    mock_repository = Mock()
    service = IncidentService(repository=mock_repository)

    incident = PaymentIncident(
        payment_id="PAY-10003",
        amount=Decimal("50.00"),
        currency="USD",
        status="INVALID",
        error_code="X",
        error_description="Test"
    )

    import pytest

    with pytest.raises(ValueError):
        service.create_incident(incident)

    mock_repository.save.assert_not_called()


def test_get_incident():
    mock_repository = Mock()
    service = IncidentService(repository=mock_repository)
    mock_repository.find_by_id.return_value = None

    with pytest.raises(ValueError):
        service.get_incident(999)

    mock_repository.find_by_id.assert_called_once_with(999)