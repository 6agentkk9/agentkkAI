import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from payment_analyzer.models.incident import PaymentIncident


class ReportGenerator:
    def __init__(self, output_dir: str | Path = "reports") -> None:
        self.output_dir = Path(output_dir)

    def generate(self, incidents: Iterable[PaymentIncident]) -> Path:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        report_path = self.output_dir / f"payment_incidents_{timestamp}.json"
        payload = [incident.model_dump(mode="json") for incident in incidents]
        with report_path.open("w", encoding="utf-8") as report_file:
            json.dump(payload, report_file, indent=2)
        return report_path
