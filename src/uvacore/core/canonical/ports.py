"""Abstract ports defining integration boundaries.

Ports declare the operations required for catalog, order, and customer flows.
Concrete implementations live in adapter layers and should be side-effecting
wrappers over platform SDKs while respecting the canonical models.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Iterable, Optional

from .dto import Product, Order, Customer


class CatalogPort(ABC):
    """Catalog operations for products."""
    @abstractmethod
    def pull_products(self, since: Optional[datetime] = None) -> Iterable[Product]:
        """Return products changed since timestamp (if provided)."""
        raise NotImplementedError

    @abstractmethod
    def push_products(self, products: Iterable[Product]) -> None:
        """Upsert canonical products into the target platform."""
        raise NotImplementedError


class OrderPort(ABC):
    """Order operations."""
    @abstractmethod
    def pull_orders(self, since: Optional[datetime] = None) -> Iterable[Order]:
        """Return orders changed since timestamp (if provided)."""
        raise NotImplementedError

    @abstractmethod
    def push_orders(self, orders: Iterable[Order]) -> None:
        """Upsert canonical orders into the target platform."""
        raise NotImplementedError


class CustomerPort(ABC):
    """Customer operations."""
    @abstractmethod
    def pull_customers(self, since: Optional[datetime] = None) -> Iterable[Customer]:
        """Return customers changed since timestamp (if provided)."""
        raise NotImplementedError