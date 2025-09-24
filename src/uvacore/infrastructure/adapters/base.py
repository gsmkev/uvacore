"""Base classes for platform adapters.

Adapters translate between platform payloads and canonical models and expose
operations declared by the core ports. Subclasses should register mapping
functions in `mapping_registry` for both directions.
"""

from __future__ import annotations

from abc import ABC
from typing import Callable, Any, Dict

from ...core.canonical.dto import Product, Order, Customer
from ...core.canonical.ports import CatalogPort, OrderPort, CustomerPort


class BaseAdapter(ABC):
    """Base class for all platform adapters.

    Holds adapter configuration and a registry of mapping functions, which
    subclasses populate via `_register_mappings`.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.mapping_registry: Dict[str, Callable[..., Any]] = {}


class BaseCatalogAdapter(BaseAdapter, CatalogPort):
    """Base implementation for catalog adapters.

    Provides helpers to map to/from canonical `Product` instances. Concrete
    adapters must implement `_register_mappings` and provide
    `to_canonical`/`from_canonical` entries.
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self._register_mappings()

    def _register_mappings(self) -> None:
        """Register platform-specific mapping functions.

        Expected keys in `mapping_registry`:
        - "to_canonical": Callable[[Any], Product]
        - "from_canonical": Callable[[Product], Any]
        """
        # To be implemented by subclasses
        return None

    def map_to_canonical(self, platform_data: Any) -> Product:
        mapper = self.mapping_registry.get("to_canonical")
        if not mapper:
            raise NotImplementedError("to_canonical mapper not implemented")
        return mapper(platform_data)

    def map_from_canonical(self, canonical_data: Product) -> Any:
        mapper = self.mapping_registry.get("from_canonical")
        if not mapper:
            raise NotImplementedError("from_canonical mapper not implemented")
        return mapper(canonical_data)