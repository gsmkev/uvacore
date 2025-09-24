"""Top-level package for uvacore.

This package provides the public API surface and semantic version for the
`uvacore` library. Downstream applications should import symbols from
subpackages (e.g., `uvacore.core`, `uvacore.infrastructure`) rather than
deep, private modules. Only the names listed in `__all__` are considered
stable and part of the public interface.
"""

__all__ = [
    "__version__",
]

__version__ = "0.1.0"

