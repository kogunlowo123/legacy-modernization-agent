"""Legacy Modernization Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class MonolithAnalysis(BaseModel):
    """MonolithAnalysis for Legacy Modernization Agent."""
    total_files: int
    total_loc: int
    coupling_score: float
    bounded_contexts: list[dict]
    tech_debt_hotspots: list[dict]


class ExtractionPlan(BaseModel):
    """ExtractionPlan for Legacy Modernization Agent."""
    service_name: str
    bounded_context: str
    phases: list[dict]
    risk_level: str
    estimated_duration: str


class ModernizationROI(BaseModel):
    """ModernizationROI for Legacy Modernization Agent."""
    current_annual_cost: float
    projected_annual_cost: float
    migration_cost: float
    payback_months: int
    risks: list[str]

