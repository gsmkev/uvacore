"""Channel configuration and source-of-truth rules.

A channel represents a tenant-bound integration with a commerce platform
(e.g., Shopify, SAP). `SourceOfTruthRule` determines data flow direction for
entity types. These models are pure data; orchestration happens in services
outside this module.
"""

from __future__ import annotations

from typing import Dict, Any, Literal, Optional
from uuid import UUID

from pydantic import BaseModel


class SourceOfTruthRule(BaseModel):
    """Defines authoritative system for a given entity type and sync direction."""
    entity_type: str  # 'product', 'order', 'customer'
    direction: Literal["ERP_MASTER", "STORE_MASTER", "BIDIRECTIONAL"]


class ChannelConfig(BaseModel):
    """Tenant-scoped integration configuration.

    - platform: integration identifier (e.g., "shopify", "sap")
    - credentials: transport-specific secret material required by adapters
    - sot_rules: per-entity `SourceOfTruthRule` used during conflict resolution
    - last_sync: ISO8601 timestamp string for last successful sync, if any
    """
    tenant_id: UUID
    platform: str  # 'shopify', 'enova', 'sap'
    platform_id: str
    credentials: Dict[str, Any]
    sot_rules: Dict[str, SourceOfTruthRule]
    enabled: bool = True
    last_sync: Optional[str] = None