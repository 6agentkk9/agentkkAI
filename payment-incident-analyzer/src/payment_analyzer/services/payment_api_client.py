import requests

from payment_analyzer.models.gateway_response import GatewayResponse


class PaymentApiError(Exception):
    """Raised when the payment gateway API cannot be queried."""


class PaymentApiClient:
    def __init__(self, base_url: str, timeout_seconds: float = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds

    def get_payment(self, payment_id: str) -> GatewayResponse:
        url = f"{self.base_url}/payments/{payment_id}"
        try:
            response = requests.get(url, timeout=self.timeout_seconds)
            response.raise_for_status()
            return GatewayResponse.model_validate(response.json())
        except requests.Timeout as exc:
            raise PaymentApiError(
                f"Gateway request timed out for {payment_id}"
            ) from exc
        except requests.RequestException as exc:
            raise PaymentApiError(
                f"Gateway request failed for {payment_id}: {exc}"
            ) from exc
        except ValueError as exc:
            raise PaymentApiError(
                f"Gateway returned invalid JSON for {payment_id}"
            ) from exc
