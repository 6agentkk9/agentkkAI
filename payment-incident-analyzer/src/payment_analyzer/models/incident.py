from datetime import datetime, timezone
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field, field_validator


class PaymentIncident(BaseModel):
    """Validated payment incident record."""

    model_config = ConfigDict(extra="forbid")

    incident_id: int | None = None
    payment_id: str = Field(min_length=1)
    amount: Decimal = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
    status: str = Field(min_length=1)
    error_code: str | None = None
    error_description: str | None = None
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, value: str) -> str:
        return value.upper()

    @field_validator("status")
    @classmethod
    def normalize_status(cls, value: str) -> str:
        return value.upper()
