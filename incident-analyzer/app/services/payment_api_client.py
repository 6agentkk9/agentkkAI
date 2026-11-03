import requests


class PaymentApiClient:

    BASE_URL = "http://localhost:8000"

    def get_payment(self, payment_id: str):

        url = f"{self.BASE_URL}/payments/{payment_id}"

        try:
            response = requests.get(
                url,
                timeout=5
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.Timeout:
            raise RuntimeError("Payment API request timed out")

        except requests.exceptions.HTTPError as error:
            raise RuntimeError(
                f"Payment API returned HTTP error: {error}"
            )

        except requests.exceptions.ConnectionError:
            raise RuntimeError("Unable to connect to Payment API")