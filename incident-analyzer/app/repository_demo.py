from decimal import Decimal

if __package__:
    from .models.incident import PaymentIncident
    from .repositories.incident_repository import IncidentRepository
else:
    from models.incident import PaymentIncident
    from repositories.incident_repository import IncidentRepository


def main():

    repository = IncidentRepository()

    # Insert incident
    incident = PaymentIncident(
        payment_id="PAY-10002",
        amount=Decimal("500.00"),
        currency="USD",
        status="FAILED",
        error_code="TIMEOUT",
        error_description="Payment gateway timeout"
    )

    saved_incident = repository.save(incident)

    print("Inserted incident:", saved_incident.incident_id)

    # Retrieve by ID
    result = repository.find_by_id(saved_incident.incident_id)

    print("\nRetrieved incident:")
    print(result)

    # Retrieve all incidents
    print("\nAll incidents:")

    for item in repository.find_all():
        print(item.payment_id, item.status, item.amount)

    # Retrieve failed incidents by Status
    print("\nFailed incidents by Status: FAILED")

    for item in repository.find_by_status("FAILED"):
        print(item.incident_id, item.payment_id, item.status, item.error_code, item.error_description)

     # Retrieve failed incidents by Error Code
    print("\nFailed incidents by Error Code: TIMEOUT")

    for item in repository.find_by_error_code("TIMEOUT"):
        print(item.incident_id, item.payment_id, item.status, item.error_code, item.error_description)

    # Retrieve an incident that doesn't exist.
    print("\nRetrieve an incident that doesn't exist:")
    result = repository.find_by_id(99999)
    print(result)


if __name__ == "__main__":
    main()