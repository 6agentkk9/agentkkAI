from decimal import Decimal

if __package__:
    from .database import get_connection
    from .models.incident import PaymentIncident
else:
    from database import get_connection
    from models.incident import PaymentIncident


def insert_incident(incident: PaymentIncident):

    with get_connection() as connection:
        connection.execute("""
            INSERT INTO payment_incidents (
                payment_id,
                amount,
                currency,
                status,
                error_code,
                error_description,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            incident.payment_id,
            str(incident.amount),
            incident.currency,
            incident.status,
            incident.error_code,
            incident.error_description,
            incident.created_at.isoformat()
        ))

    print("Payment incident inserted successfully")


def main():
    incident = PaymentIncident(
        payment_id="PAY-10001",
        amount=Decimal("250.00"),
        currency="USD",
        status="FAILED",
        error_code="INSUFFICIENT_FUNDS",
        error_description="Insufficient customer balance"
    )

    insert_incident(incident)


if __name__ == "__main__":
    main()