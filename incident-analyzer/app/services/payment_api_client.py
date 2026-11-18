import requests
import os
from dotenv import load_dotenv
from decimal import Decimal
load_dotenv()

class PaymentApiClient:

    # BASE_URL = "http://localhost:8000"
    BASE_URL = os.getenv(
        "PAYMENT_API_BASE_URL",
        "http://localhost:8000"
    )

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

    @staticmethod
    def calculate_refund_amount(
        amount: Decimal,
        refund_percentage: int | float
    ) -> Decimal:

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if not 1 <= refund_percentage <= 100:
            raise ValueError("Invalid refund percentage")

        percentage = Decimal(str(refund_percentage))

        return amount * percentage / Decimal("100")