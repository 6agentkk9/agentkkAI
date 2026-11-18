from pydantic import BaseModel, ConfigDict


class GatewayResponse(BaseModel):
    """Normalized response returned by a payment gateway."""

    model_config = ConfigDict(extra="ignore")

    payment_id: str
    status: str
    response_code: str | None = None
    message: str | None = None
