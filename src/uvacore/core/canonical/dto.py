"""Canonical DTOs for products, variants, customers, and orders.

Models are immutable (frozen) to ensure referential transparency across
boundaries. Fields intentionally avoid business logic. Mapping between
platform-specific payloads and these DTOs is performed by adapters.
"""

from __future__ import annotations

from typing import Optional, Dict, List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class Money(BaseModel):
    """Monetary value.

    - currency: ISO 4217 alpha-3 code (e.g., "USD")
    - amount: decimal amount in major units. Precision depends on source.
    """
    currency: str  # ISO 4217
    amount: float

    model_config = ConfigDict(frozen=True)


class Variant(BaseModel):
    """Product variant in the catalog.

    Attributes capture SKU-level granularity and optional platform attributes.
    Custom attributes are stored in `attributes` as a flat dict.
    """
    id: UUID
    sku: str
    price: Money
    barcode: Optional[str] = None
    attributes: Dict[str, str] = Field(default_factory=dict)

    model_config = ConfigDict(frozen=True)


class Product(BaseModel):
    """Canonical product shape.

    Contains a list of `Variant` items. Tags are free-form labels.
    """
    id: UUID
    title: str
    description: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    variants: List[Variant] = Field(default_factory=list)

    model_config = ConfigDict(frozen=True)


class Customer(BaseModel):
    """Canonical customer identity profile."""
    id: UUID
    email: str
    first_name: str
    last_name: str

    model_config = ConfigDict(frozen=True)


class Order(BaseModel):
    """Canonical order envelope.

    - line_items: implementation-defined list of lines; adapters normalize as needed
    - status: lifecycle string (e.g., "created", "paid", "fulfilled")
    """
    id: UUID
    customer_id: UUID
    line_items: List[Dict] = Field(default_factory=list)
    status: str

    model_config = ConfigDict(frozen=True)