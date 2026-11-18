from decimal import Decimal
import pytest
from pydantic import ValidationError

from payment_analyzer.models.incident import PaymentIncident


def test_incident_normalizes_currency_and_status():
    incident = PaymentIncident(
        payment_id="PAY-1",
        amount=Decimal("12.50"),
        currency="usd",
        status="failed",
    )
    assert incident.currency == "USD"
    assert incident.status == "FAILED"


def test_incident_rejects_non_positive_amount():
    with pytest.raises(ValidationError):
        PaymentIncident(
            payment_id="PAY-1",
            amount=Decimal("0"),
            currency="USD",
            status="FAILED",
        )
