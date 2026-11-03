import json
import logging

if __package__:
    from .repositories.incident_repository import IncidentRepository
    from .services.payment_api_client import PaymentApiClient
    from .services.gateway_response_mapper import map_gateway_response
    from .services.ai_analyzer import AIIncidentAnalyzer
    from .services.report_generator import ReportGenerator
    from .logging_config import setup_logging
else:
    from repositories.incident_repository import IncidentRepository
    from services.payment_api_client import PaymentApiClient
    from services.gateway_response_mapper import map_gateway_response
    from services.ai_analyzer import AIIncidentAnalyzer
    from services.report_generator import ReportGenerator
    from logging_config import setup_logging


def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Payment Incident Analyzer started")

    # Step 1: Retrieve incident from SQLite
    repository = IncidentRepository()

    incident = repository.find_by_id(1)

    if incident is None:
        print("Incident not found")
        return

    # Step 2: Retrieve payment information from gateway
    payment_client = PaymentApiClient()

    gateway_data = payment_client.get_payment(
        incident.payment_id
    )

    # Step 3: Convert JSON into Python model
    gateway_response = map_gateway_response(gateway_data)

    # Step 4: Ask AI to analyze the incident
    analyzer = AIIncidentAnalyzer()

    analysis = analyzer.analyze(
        incident,
        gateway_response
    )

    # Step 5: Display AI analysis
    
    # print("\nPAYMENT INCIDENT AI ANALYSIS")
    # print("============================")
    # print(analysis)

    # analysis = analyzer.analyze(
    #     incident,
    #     gateway_response
    # )

    print("\nSTRUCTURED PAYMENT INCIDENT ANALYSIS")
    print("====================================")

    print("Payment ID:", analysis.payment_id)
    print("Category:", analysis.incident_category)
    print("Root Cause:", analysis.root_cause)
    print("Confidence:", analysis.confidence)

    print("\nEvidence:")

    for item in analysis.evidence:
        print("-", item)

    print("\nRecommended Actions:")

    for action in analysis.recommended_actions:
        print("-", action)

    print("\nRetry Recommendation:")
    print(analysis.retry_recommendation)

    # JSON REPORT
    logger.info(
    "Generating report for payment_id=%s",
    incident.payment_id
    )
    
    report_generator = ReportGenerator()

    report_path = report_generator.generate(
        incident,
        analysis
    )

    print("\nJSON REPORT GENERATED")
    print("=====================")
    print("Report location:", report_path)

    with open(report_path, "r", encoding="utf-8") as file:
        loaded_report = json.load(file)

    print("Validated payment ID:", loaded_report["incident"]["payment_id"])
 
    logger.info(
    "Report generated for payment_id=%s",
    incident.payment_id
)

if __name__ == "__main__":
    main()