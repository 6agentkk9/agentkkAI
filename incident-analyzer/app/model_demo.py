from decimal import Decimal

if __package__:
    from .models.incident import PaymentIncident
else:
    from models.incident import PaymentIncident


def main():
    incident = PaymentIncident(
        payment_id="PAY-10001",
        amount=Decimal("-250.00"),
        currency="usd",
        status="FAILED",
        error_code="INSUFFICIENT_FUNDS",
        error_description="Insufficient customer balance"
    )

    print("Payment Incident")
    print("----------------")
    print(f"Payment ID: {incident.payment_id}")
    print(f"Amount: {incident.amount}")
    print(f"Currency: {incident.currency}")
    print(f"Status: {incident.status}")
    print(f"Error Code: {incident.error_code}")
    print(f"Description: {incident.error_description}")
    print(f"Created At: {incident.created_at}")


if __name__ == "__main__":
    main()