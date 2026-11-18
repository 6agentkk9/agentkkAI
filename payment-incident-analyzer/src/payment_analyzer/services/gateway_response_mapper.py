from payment_analyzer.models.gateway_response import GatewayResponse
from payment_analyzer.models.incident import PaymentIncident


def apply_gateway_response(
    incident: PaymentIncident,
    response: GatewayResponse,
) -> PaymentIncident:
    """Return a copy of an incident enriched with gateway status details."""
    return incident.model_copy(
        update={
            "status": response.status.upper(),
            "error_code": response.response_code,
            "error_description": response.message,
        }
    )
