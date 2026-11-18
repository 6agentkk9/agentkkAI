from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

if __package__ and __package__.startswith("app."):
    from ..models.refund_reason import RefundReason
elif __package__:
    from .refund_reason import RefundReason
else:
    from refund_reason import RefundReason


class RefundRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    payment_id: str
    refund_amount: Decimal = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
    reason: RefundReason