import pytest
from decimal import Decimal
from app.refund_validation_error import RefundValidationError
from app.refund_validation_error import validate_refund

# rootdir: G:\agentkkAI run
# python -m pytest -v .\incident-analyzer\tests

@pytest.mark.parametrize(
    "payment_id, amount, expected_valid",
    [
        ("PAY-10001", Decimal("100.00"), True),
        (None, Decimal("100.00"), False),
        ("PAY-10001", Decimal("0"), False),
        ("PAY-10001", Decimal("15000"), False),
    ],
)
def test_validate_refund(payment_id, amount, expected_valid):
    if expected_valid:
        assert validate_refund(payment_id, amount) is True
    else:
        with pytest.raises(ValueError):
            validate_refund(payment_id, amount)