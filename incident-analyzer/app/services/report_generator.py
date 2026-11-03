import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from venv import logger

class ReportGenerator:
    
    logger = logging.getLogger(__name__)

    def __init__(self):
        # Project root is two levels above this file.
        project_root = Path(__file__).resolve().parents[2]
        self.reports_dir = project_root / "reports"

    def generate(self, incident, analysis):
        self.reports_dir.mkdir(parents=True, exist_ok=True)

        generated_at = datetime.now(timezone.utc)

        report = {
            "report_metadata": {
                "generated_at": generated_at.isoformat(),
                "report_type": "PAYMENT_INCIDENT_ANALYSIS"
            },
            "incident": {
                "incident_id": incident.incident_id,
                "payment_id": incident.payment_id,
                "amount": str(incident.amount),
                "currency": incident.currency,
                "status": incident.status,
                "error_code": incident.error_code,
                "error_description": incident.error_description,
                "created_at": incident.created_at.isoformat()
            },
            "analysis": analysis.model_dump()
        }

        if not incident.payment_id:
            logger.error("Cannot generate report without payment ID")
            raise ValueError("Payment ID is required")

        # Timestamp makes each report filename unique.
        timestamp = generated_at.strftime("%Y%m%d_%H%M%S_%f")
        safe_payment_id = "".join(
            char for char in incident.payment_id
            if char.isalnum() or char in ("-", "_")
        )

        filename = (
            f"incident_{incident.incident_id}_"
            f"{safe_payment_id}_{timestamp}.json"
        )

        report_path = self.reports_dir / filename

        try:
            with report_path.open("w", encoding="utf-8") as file:
                json.dump(report, file, indent=4, ensure_ascii=False)
        except OSError:
            logger.exception (
                "Unable to write report for payment_id=%s",
                incident.payment_id
            )
            raise

        return report_path