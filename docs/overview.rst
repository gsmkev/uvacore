Overview
========

`uvacore` provides:

- Canonical DTOs and events
- Abstract ports for integration boundaries
- Channel configuration
- Infrastructure base classes and an in-memory event outbox

Architecture
------------

The library follows a ports-and-adapters architecture. Core exposes immutable
models and abstract interfaces; infrastructure provides concrete side-effecting
implementations.

Dependency Injection
--------------------

Use :class:`uvacore.config.di.CoreContainer` to wire adapters and repositories.

