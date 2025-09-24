def test_basic_imports():
    import uvacore
    from uvacore.core.canonical.dto import Product, Variant, Money
    from uvacore.core.canonical.events import ProductUpdated
    from uvacore.core.canonical.ports import CatalogPort
    from uvacore.infrastructure.event_system.outbox import InMemoryOutboxRepository

    assert isinstance(uvacore.__version__, str)
    assert Money(currency="USD", amount=1.0)
    assert InMemoryOutboxRepository()