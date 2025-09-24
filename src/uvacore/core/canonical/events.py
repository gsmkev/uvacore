"""Canonical event contracts used by the event system.

Events carry a typed payload (`data`) and `EventMetadata` for observability,
multi-tenant routing, and idempotency. Concrete event classes provide a
stable `type` literal for downstream consumers.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Literal
from uuid import UUID

from pydantic import BaseModel


class EventMetadata(BaseModel):
    """Transport-agnostic event headers for tracing and routing."""
    occurred_at: datetime
    idempotency_key: UUID
    trace_id: UUID
    tenant_id: UUID
    channel_id: UUID


class CanonicalEvent(BaseModel):
    """Base event with generic data payload and metadata."""
    type: str
    version: str = "v1"
    data: Dict[str, Any]
    metadata: EventMetadata


class ProductUpdated(CanonicalEvent):
    """Product change observed in a source system."""
    type: Literal["ProductUpdated"] = "ProductUpdated"


class OrderCreated(CanonicalEvent):
    """Order creation event emitted by a source system."""
    type: Literal["OrderCreated"] = "OrderCreated"


class CustomerSynced(CanonicalEvent):
    """Customer synchronization event across systems."""
    type: Literal["CustomerSynced"] = "CustomerSynced"