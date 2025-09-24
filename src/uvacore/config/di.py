"""Dependency Injection container wiring for uvacore.

This module exposes `CoreContainer`, a `dependency_injector` container that
centralizes configuration and wiring for repositories and adapters. Client
applications can extend or override providers to bind concrete platform
adapters and event dispatchers.
"""

from __future__ import annotations

from dependency_injector import containers, providers

from ..infrastructure.adapters.base import BaseCatalogAdapter
from ..infrastructure.event_system.outbox import InMemoryOutboxRepository, OutboxRepository


class CoreContainer(containers.DeclarativeContainer):
    """Composition root for application services and infrastructure.

    Exposes providers for configuration, adapter factory registry, and the
    outbox repository implementation. Override providers in application code
    to inject environment-specific dependencies.
    """

    config = providers.Configuration()

    # Adapter registry (placeholders; concrete adapters can be wired by clients)
    adapter_factory = providers.Dict(
        # Example: "shopify": providers.Factory(ShopifyAdapter)
    )

    # Repository implementations
    outbox_repository: providers.Provider[OutboxRepository] = providers.Singleton(
        InMemoryOutboxRepository
    )

    # Event system placeholders (to be implemented by apps)
    # event_dispatcher = providers.Singleton(EventDispatcher)