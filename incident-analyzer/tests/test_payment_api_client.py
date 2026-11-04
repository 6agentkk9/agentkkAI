from unittest.mock import Mock, patch

import requests
import pytest

from app.services.payment_api_client import PaymentApiClient

# rootdir: G:\agentkkAI run 
# python -m pytest -v .\incident-analyzer\tests

@patch("app.services.payment_api_client.requests.get")
def test_get_payment_success(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "payment_id": "PAY-10001",
        "gateway": "MockGateway",
        "gateway_status": "DECLINED",
        "response_code": "51",
        "response_message": "Insufficient funds"
    }

    mock_get.return_value = mock_response

    client = PaymentApiClient()
    result = client.get_payment("PAY-10001")

    assert result["payment_id"] == "PAY-10001"
    assert result["response_code"] == "51"

    mock_get.assert_called_once_with(
        "http://localhost:8000/payments/PAY-10001",
        timeout=5
    )


@patch("app.services.payment_api_client.requests.get")
def test_get_payment_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout

    client = PaymentApiClient()

    with pytest.raises(RuntimeError, match="timed out"):
        client.get_payment("PAY-10001")