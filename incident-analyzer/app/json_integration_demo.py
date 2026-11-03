if __package__:
    from .services.gateway_response_mapper import map_gateway_response
    from .services.payment_api_client import PaymentApiClient
else:
    from services.gateway_response_mapper import map_gateway_response
    from services.payment_api_client import PaymentApiClient




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


if __name__ == "__main__":
    main()