# unit test for payment.py
# run ---> python -m pytest

# (All)  python -m pytest 
# (File) python -m pytest test_payment.py


# Full Use parameterized tests
import pytest
from payment import calculate_fee
@pytest.mark.parametrize(
    "amount, fee",
    [
        (10, 0.2),
        (500, 10),
        (0, 0)
    ]
)

def test_calculate_fee(amount, fee):
        assert calculate_fee(amount) == fee

def test_negative_calculate_fee():
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        calculate_fee(-100)




# other tests
import pytest
from payment import calculate_fee

def test_normal_payment():
    assert calculate_fee(100) == 2


def test_large_payment():
    assert calculate_fee(1000) == 20


def test_zero_payment():
    assert calculate_fee(0) == 0

def test_negative_amount_message():

    with pytest.raises(
        ValueError,
        match="Amount cannot be negative"
    ): 
        calculate_fee(-100)

# Use fixtures
@pytest.fixture
def payment():
    return {
        "payment_id": 1001,
        "amount": 250,
        "status": "SUCCESS"
    }

def test_payment_id(payment):
    assert payment["payment_id"] == 1001


def test_payment_amount(payment):
    assert payment["amount"] == 250


def test_payment_status(payment):
    assert payment["status"] == "SUCCESS"


from unittest.mock import patch
from payment_service import get_payment


