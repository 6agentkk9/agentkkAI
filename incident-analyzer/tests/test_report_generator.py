from decimal import Decimal
from unittest.mock import Mock

from app.models.incident import PaymentIncident
from app.services.report_generator import ReportGenerator

# rootdir: G:\agentkkAI run 
# python -m pytest -v .\incident-analyzer\tests

def test_generate_json_report(tmp_path):
    incident = PaymentIncident(
        payment_id="PAY-10001",
        amount=Decimal("125.50"),
        currency="USD",
        status="FAILED",
        error_code="51",
        error_description="Insufficient funds"
    )

    analysis = Mock()
    analysis.model_dump.return_value = {
        "payment_id": "PAY-10001",
        "incident_category": "ISSUER_DECLINE",
        "root_cause": "Issuer declined transaction",
        "confidence": "HIGH",
        "evidence": ["Response code 51"],
        "recommended_actions": ["Review issuer response"],
        "retry_recommendation": "Do not automatically retry"
    }

    generator = ReportGenerator()

    # Redirect output to the test's temporary directory.
    generator.reports_dir = tmp_path

    report_path = generator.generate(incident, analysis)

    assert report_path.exists()
    assert report_path.suffix == ".json"

    import json

    with report_path.open(encoding="utf-8") as file:
        report = json.load(file)

    assert report["incident"]["payment_id"] == "PAY-10001"
    assert report["analysis"]["incident_category"] == "ISSUER_DECLINE"