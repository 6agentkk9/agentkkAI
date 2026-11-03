from decimal import Decimal

if __package__:
    from .models.incident import PaymentIncident
    from .services.incident_service import IncidentService
else:
    from models.incident import PaymentIncident
    from services.incident_service import IncidentService


def main():

    service = IncidentService()

    # Create a new incident
    incident = PaymentIncident(
        payment_id="PAY-10003",
        amount=Decimal("750.00"),
        currency="USD",
        status="FAILED",
        error_code="GATEWAY_TIMEOUT",
        error_description="External payment gateway timeout"
    )

    saved = service.create_incident(incident)

    print("Created incident:", saved.incident_id)

    # Retrieve incident
    result = service.get_incident(saved.incident_id)

    print("\nIncident details:")
    print(result)

    # Retrieve failed incidents
    print("\nFailed incidents:")

    for item in service.get_failed_incidents():
        print(item.payment_id, item.error_code)

    # Display summary
    print("\nIncident Summary:")

    summary = service.get_incident_summary()

    for key, value in summary.items():
        print(f"{key}: {value}")


   # Create an invalid incident
    print("\nCreating Invalid incident:")

    invalid_incident = PaymentIncident(
        payment_id="PAY-10003",
        amount=Decimal("750.00"),
        currency="USD",
        status="PROCESSING",
        error_code="GATEWAY_TIMEOUT",
        error_description="External payment gateway timeout"
    )

    saved = service.create_incident(invalid_incident)
    print("Invalid incident:", saved.incident_id)


if __name__ == "__main__":
    main()