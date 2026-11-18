import json
from decimal import Decimal

from payment_analyzer.models.incident import PaymentIncident
from payment_analyzer.services.report_generator import ReportGenerator


def test_report_generator_writes_json(tmp_path):
    incident = PaymentIncident(
        payment_id="PAY-7",
        amount=Decimal("9.99"),
        currency="USD",
        status="DECLINED",
    )

    path = ReportGenerator(tmp_path).generate([incident])

    assert path.exists()
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data[0]["payment_id"] == "PAY-7"
    assert data[0]["amount"] == "9.99"
