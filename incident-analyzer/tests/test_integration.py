import json
from decimal import Decimal
from types import SimpleNamespace

from app.database import create_tables
from app.models.incident import PaymentIncident
from app.repositories.incident_repository import IncidentRepository
from app.services.incident_service import IncidentService
from app.services.payment_api_client import PaymentApiClient
from app.services.gateway_response_mapper import map_gateway_response
from app.services.report_generator import ReportGenerator

# rootdir: G:\agentkkAI run 
# python -m pytest -v .\incident-analyzer\tests

def test_payment_incident_integration(tmp_path):
    # 1. Create an isolated test database.
    db_path = tmp_path / "test_incidents.db"
    create_tables(db_path)

    # 2. Use the real repository and service.
    repository = IncidentRepository(db_path=db_path)
    service = IncidentService(repository=repository)

    incident = PaymentIncident(
        payment_id="PAY-10001",
        amount=Decimal("125.50"),
        currency="USD",
        status="FAILED",
        error_code="51",
        error_description="Insufficient funds"
    )

    saved_incident = service.create_incident(incident)

    assert saved_incident.incident_id is not None

    # 3. Read the incident back from SQLite.
    retrieved_incident = service.get_incident(
        saved_incident.incident_id
    )

    assert retrieved_incident.payment_id == "PAY-10001"
    assert retrieved_incident.amount == Decimal("125.50")

    # 4. Call the real local mock payment API.
    api_client = PaymentApiClient()
    payment_data = api_client.get_payment("PAY-10001")

    gateway_response = map_gateway_response(payment_data)

    assert gateway_response.payment_id == "PAY-10001"
    assert gateway_response.response_code == "51"

    # 5. Use a predictable AI result instead of calling OpenAI.
    fake_analysis = SimpleNamespace(
        model_dump=lambda: {
            "payment_id": "PAY-10001",
            "incident_category": "ISSUER_DECLINE",
            "root_cause": "Issuer declined the transaction",
            "confidence": "HIGH",
            "evidence": ["Gateway response code 51"],
            "recommended_actions": ["Review issuer response"],
            "retry_recommendation": "Do not automatically retry"
        }
    )

    # 6. Generate a report using the real report generator.
    generator = ReportGenerator()
    generator.reports_dir = tmp_path / "reports"

    report_path = generator.generate(
        retrieved_incident,
        fake_analysis
    )

    # 7. Verify the generated report.
    assert report_path.exists()

    with report_path.open(encoding="utf-8") as file:
        report = json.load(file)

    assert report["incident"]["payment_id"] == "PAY-10001"
    assert report["analysis"]["incident_category"] == "ISSUER_DECLINE"