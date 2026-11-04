import pytest
from decimal import Decimal
from app.models.incident import PaymentIncident

# rootdir: G:\agentkkAI run 
# python -m pytest -v .\incident-analyzer\tests

def test_create_valid_incident():
    incident = PaymentIncident(
        payment_id="PAY-10001",
        amount=Decimal("125.50"),
        currency="usd",
        status="FAILED",
        error_code="51",
        error_description="Insufficient funds"
    )

    assert incident.payment_id == "PAY-10001"
    assert incident.amount == Decimal("125.50")
    assert incident.currency == "USD"


def test_reject_zero_amount():
    with pytest.raises(ValueError):
        PaymentIncident(
            payment_id="PAY-10001",
            amount=Decimal("0"),
            currency="USD",
            status="FAILED",
            error_code="51",
            error_description="Invalid amount"
        )