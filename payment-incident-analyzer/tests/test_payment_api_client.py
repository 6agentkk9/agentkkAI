import requests
import pytest

from payment_analyzer.services.payment_api_client import PaymentApiClient, PaymentApiError


def test_gateway_client_translates_connection_error(monkeypatch):
    def fake_get(*args, **kwargs):
        raise requests.ConnectionError("connection refused")

    monkeypatch.setattr(requests, "get", fake_get)
    client = PaymentApiClient("http://localhost:8000")

    with pytest.raises(PaymentApiError):
        client.get_payment("PAY-1")
