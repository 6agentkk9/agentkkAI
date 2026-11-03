from decimal import Decimal

if __package__ and __package__.startswith("app."):
    from ..models.gateway_response import GatewayResponse
else:
    from models.gateway_response import GatewayResponse


def map_gateway_response(data: dict) -> GatewayResponse:

    return GatewayResponse(
        payment_id=data.get("payment_id", ""),
        gateway=data.get("gateway", "UNKNOWN"),
        gateway_status=data.get("gateway_status", "UNKNOWN"),
        response_code=data.get("response_code", "UNKNOWN"),
        response_message=data.get("response_message", ""),
        amount=(
            Decimal(data["amount"])
            if data.get("amount") is not None
            else None
        ),
        currency=data.get("currency")
    )