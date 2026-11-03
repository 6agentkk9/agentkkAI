from dataclasses import dataclass


@dataclass
class IncidentAnalysis:

    payment_id: str
    incident_category: str
    root_cause: str
    confidence: str
    evidence: list[str]
    recommended_actions: list[str]
    retry_recommendation: str