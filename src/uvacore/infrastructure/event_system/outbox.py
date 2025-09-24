"""Event outbox repository abstractions and in-memory implementation.

Implements the transactional outbox pattern to persist events for reliable
delivery. The `InMemoryOutboxRepository` is suitable for testing and local
development only; production systems should provide durable storage-backed
implementations.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from ...core.canonical.events import CanonicalEvent


class OutboxEvent:
    """Persistent representation of an event awaiting dispatch."""
    def __init__(self, event: CanonicalEvent, status: str = "PENDING"):
        self.id: UUID = uuid4()
        self.event = event
        self.status = status
        self.attempts = 0
        self.last_attempt: Optional[datetime] = None
        self.error: Optional[str] = None


class OutboxRepository(ABC):
    """Storage contract for the event outbox."""
    @abstractmethod
    def save(self, event: CanonicalEvent) -> OutboxEvent:
        """Persist a new event in PENDING state and return its envelope."""
        raise NotImplementedError

    @abstractmethod
    def get_pending_events(self, limit: int = 100) -> List[OutboxEvent]:
        """Return up to `limit` events with status PENDING."""
        raise NotImplementedError

    @abstractmethod
    def mark_as_processed(self, event_id: UUID) -> None:
        """Mark event as SENT and record last attempt timestamp."""
        raise NotImplementedError

    @abstractmethod
    def mark_failed(self, event_id: UUID, error: str) -> None:
        """Mark event as FAILED, increment attempts, and record error details."""
        raise NotImplementedError


class InMemoryOutboxRepository(OutboxRepository):
    def __init__(self) -> None:
        self._events: List[OutboxEvent] = []

    def save(self, event: CanonicalEvent) -> OutboxEvent:
        ob = OutboxEvent(event)
        self._events.append(ob)
        return ob

    def get_pending_events(self, limit: int = 100) -> List[OutboxEvent]:
        return [e for e in self._events if e.status == "PENDING"][:limit]

    def mark_as_processed(self, event_id: UUID) -> None:
        for e in self._events:
            if e.id == event_id:
                e.status = "SENT"
                e.last_attempt = datetime.utcnow()
                e.error = None
                return

    def mark_failed(self, event_id: UUID, error: str) -> None:
        for e in self._events:
            if e.id == event_id:
                e.status = "FAILED"
                e.attempts += 1
                e.last_attempt = datetime.utcnow()
                e.error = error
                return