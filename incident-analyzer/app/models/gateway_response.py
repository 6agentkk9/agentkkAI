from dataclasses import dataclass
from decimal import Decimal


@dataclass
class GatewayResponse:
    payment_id: str
    gateway: str
    gateway_status: str
    response_code: str
    response_message: str
    amount: Decimal | None = None
    currency: str | None = None