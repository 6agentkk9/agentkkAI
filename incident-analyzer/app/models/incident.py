from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal


@dataclass
class PaymentIncident:
    payment_id: str
    amount: Decimal
    currency: str
    status: str
    error_code: str
    error_description: str

    incident_id: int | None = None

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Payment amount must be greater than zero")

        self.currency = self.currency.upper()