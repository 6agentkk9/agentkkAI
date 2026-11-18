from decimal import Decimal
from unittest import result


if __package__:
    from .services.gateway_response_mapper import map_gateway_response
    from .services.payment_api_client import PaymentApiClient
    from .models.payment_status import PaymentStatus
    from .models.payment_request import PaymentRequest
    from .models.refund_reason import RefundReason
    from .models.refund_request import RefundRequest
else:
    from services.gateway_response_mapper import map_gateway_response
    from services.payment_api_client import PaymentApiClient
    from models.payment_status import PaymentStatus
    from models.payment_request import PaymentRequest
    from models.refund_reason import RefundReason
    from models.refund_request import RefundRequest

def main():

    client = PaymentApiClient()

    # Retrieve JSON from payment API
    response_data = client.get_payment("PAY-10001")

    # Map JSON into structured Python object
    gateway_response = map_gateway_response(response_data)

    print("Structured Gateway Response")
    print("----------------------------")

    print("Payment ID:", gateway_response.payment_id)
    print("Gateway:", gateway_response.gateway)
    print("Status:", gateway_response.gateway_status)
    print("Response Code:", gateway_response.response_code)
    print("Message:", gateway_response.response_message)

    print("validate calculate_refund_amount")
    refund_amount = client.calculate_refund_amount(Decimal("125.50"), 50)
    print(refund_amount)

    print("validate PaymentStatus Enum")
    status = PaymentStatus.FAILED
    print(status)
    print(status.value)



    print("validate PaymentRequest")
    valid_request = PaymentRequest(
        payment_id="PAY-10001",
        amount="125.50",
        # amount="-125.50",
        currency="USD",
        status="FAILED"
    )
    print(valid_request.amount)
    print(valid_request.model_dump())

    print("validate RefundRequest")
    refund = RefundRequest(
        payment_id="PAY-10001",
        refund_amount=Decimal("25.50"),
        # refund_amount=Decimal("-25.50"),
        currency="USD",
        reason=RefundReason.DUPLICATE
    )

    print(refund)
    print(refund.model_dump())

if __name__ == "__main__":
    main()