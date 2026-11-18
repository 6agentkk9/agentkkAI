from pydantic import BaseModel, ConfigDict, Field


class IncidentAnalysis(BaseModel):
    """Structured incident analysis suitable for JSON reporting."""

    model_config = ConfigDict(extra="forbid")

    summary: str
    likely_cause: str
    recommended_actions: list[str] = Field(default_factory=list)
    requires_manual_review: bool = True
