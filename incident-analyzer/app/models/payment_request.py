from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

if __package__ and __package__.startswith("app."):
    from ..models.payment_status import PaymentStatus
elif __package__:
    from .payment_status import PaymentStatus
else:
    from payment_status import PaymentStatus

class PaymentRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    payment_id: str
    amount: Decimal = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
    status: PaymentStatus
