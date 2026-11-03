import json
from decimal import Decimal


if __package__:
    from .services.gateway_response_mapper import map_gateway_response
    from .services.payment_api_client import PaymentApiClient
else:
    from services.gateway_response_mapper import map_gateway_response
    from services.payment_api_client import PaymentApiClient

def main():

    client = PaymentApiClient()

    try:
        print("Payment PAY-10004 test")
        print("-------------------------")
        response_data = client.get_payment("PAY-10004")
        payment = map_gateway_response(response_data)
        print(payment.payment_id)
        print(payment.gateway)
        print(payment.gateway_status)
        print(payment.response_code)
        print(payment.response_message)
        if payment.amount is not None and not isinstance(payment.amount, Decimal):
            raise TypeError("Payment amount must be a Decimal")
        print(f"Amount: {payment.amount} ({type(payment.amount).__name__})")
        print(payment.currency)

        print("Payment Gateway Response")
        print("-------------------------")
        payment = client.get_payment("PAY-10001")
        for key, value in payment.items():
            print(f"{key}: {value}")


        print("Payment Gateway Error Response")
        payment = client.get_payment("PAY-99999")
        print("-------------------------")

        for key, value in payment.items():
            print(f"{key}: {value}")



    except RuntimeError as error:
        print("API Error:", error)


if __name__ == "__main__":
    main()