import argparse
import logging
from decimal import Decimal

from payment_analyzer.config.settings import settings
from payment_analyzer.models.incident import PaymentIncident
from payment_analyzer.repositories.incident_repository import IncidentRepository
from payment_analyzer.services.incident_service import IncidentService
from payment_analyzer.services.payment_api_client import PaymentApiClient, PaymentApiError
from payment_analyzer.services.report_generator import ReportGenerator
from payment_analyzer.utils.logging_config import configure_logging


def seed_sample_data(service: IncidentService) -> None:
    samples = [
        PaymentIncident(
            payment_id="PAY-10001", amount=Decimal("125.50"),
            currency="USD", status="DECLINED", error_code="51",
            error_description="Insufficient funds",
        ),
        PaymentIncident(
            payment_id="PAY-10002", amount=Decimal("89.99"),
            currency="USD", status="PENDING", error_code="TIMEOUT",
            error_description="Gateway timeout",
        ),
        PaymentIncident(
            payment_id="PAY-10003", amount=Decimal("250.00"),
            currency="USD", status="FAILED", error_code="96",
            error_description="System malfunction",
        ),
    ]
    for incident in samples:
        service.create_incident(incident)


def main() -> None:
    parser = argparse.ArgumentParser(description="Payment Incident Analyzer")
    parser.add_argument("--init-db", action="store_true", help="Create database tables")
    parser.add_argument("--seed", action="store_true", help="Insert sample incidents")
    parser.add_argument("--list", action="store_true", help="List stored incidents")
    parser.add_argument("--report", action="store_true", help="Generate a JSON report")
    parser.add_argument("--check-gateway", metavar="PAYMENT_ID", help="Query mock/real gateway")
    args = parser.parse_args()

    configure_logging(settings.log_level)
    logger = logging.getLogger(__name__)

    repository = IncidentRepository(settings.database_path)
    service = IncidentService(repository)

    if args.init_db or args.seed or args.list or args.report:
        repository.create_tables()

    if args.seed:
        seed_sample_data(service)
        print("Sample incidents inserted.")

    if args.list:
        for incident in service.list_incidents():
            print(incident.model_dump(mode="json"))

    if args.report:
        path = ReportGenerator("reports").generate(service.list_incidents())
        print(f"Report written to: {path}")

    if args.check_gateway:
        client = PaymentApiClient(
            settings.payment_api_base_url,
            settings.payment_api_timeout_seconds,
        )
        try:
            result = client.get_payment(args.check_gateway)
            print(result.model_dump())
        except PaymentApiError as exc:
            logger.error("%s", exc)
            raise SystemExit(1) from exc

    if not any((args.init_db, args.seed, args.list, args.report, args.check_gateway)):
        parser.print_help()


if __name__ == "__main__":
    main()
