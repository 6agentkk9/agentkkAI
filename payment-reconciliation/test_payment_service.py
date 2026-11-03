
# You can test it without calling the real API:
# Important: Mocking prevents the network call, but you should also test how your code handles HTTP errors and timeouts.


# (All)  python -m pytest 
# (File) python -m pytest test_payment_service.py

from unittest.mock import patch
from payment_service import get_payment

@patch("payment_service.requests.get")
def test_get_payment(mock_get):

    mock_get.return_value.json.return_value = {
        "paymentId": 1001,
        "status": "SUCCESS"
    }

    result = get_payment(1001)

    assert result["paymentId"] == 1001
    assert result["status"] == "SUCCESS"