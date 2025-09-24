# uvacore

Core library implementing canonical domain contracts and ports/adapters for commerce integrations.

`uvacore` defines:

- Canonical DTOs and events (`uvacore.core.canonical`)
- Abstract ports for catalog, orders, customers (`uvacore.core.canonical.ports`)
- Channel configuration models (`uvacore.core.channel`)
- Infrastructure primitives for adapters and event outbox (`uvacore.infrastructure`)

## Architecture

`uvacore` follows a ports-and-adapters (hexagonal) architecture:

- Core exposes immutable data models and abstract interfaces.
- Infrastructure implements adapters that map platform payloads to canonical forms.
- An event outbox provides reliable event persistence and dispatch decoupling.

Applications wire concrete implementations via the dependency injection container
`uvacore.config.di.CoreContainer`.

### Key Modules

- `uvacore.core.canonical.dto`: Product, Variant, Customer, Order models
- `uvacore.core.canonical.events`: CanonicalEvent and concrete event types
- `uvacore.core.canonical.ports`: Integration boundaries for pull/push flows
- `uvacore.core.channel`: Tenant-bound channel and source-of-truth rules
- `uvacore.infrastructure.adapters.base`: Base classes for platform adapters
- `uvacore.infrastructure.event_system.outbox`: Outbox repository contracts

## Usage

Implement a platform adapter by extending `BaseCatalogAdapter` and binding it
in the DI container:

```python
from uvacore.config.di import CoreContainer

container = CoreContainer()
container.adapter_factory.update({
    "shopify": YourShopifyAdapterFactory,
})

outbox = container.outbox_repository()
```

## Development

- Create venv and install dev deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

- Run checks:

```bash
pytest
mypy src/
black src/ tests/
```

## Documentation

Build the documentation locally (requires Sphinx):

```bash
pip install -e ".[dev]"
pip install -r docs/requirements.txt
make -C docs html
open docs/_build/html/index.html
```

Read the Docs configuration is provided in `.readthedocs.yaml`.
