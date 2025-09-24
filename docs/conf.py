"""Sphinx configuration for uvacore documentation.

Configured for Read the Docs theme, autodoc, napoleon, myst, and type hints.
"""

from __future__ import annotations

import os
import sys
from datetime import datetime

# Ensure package is importable for autodoc (src layout)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

project = "uvacore"
author = "UvaSoft"
copyright = f"{datetime.utcnow().year}, {author}"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "myst_parser",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
autodoc_member_order = "bysource"
add_module_names = False
autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_param = True
napoleon_use_rtype = True

templates_path = ["_templates"]
exclude_patterns: list[str] = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "style_external_links": True,
    "sticky_navigation": True,
}

# Pygments styles for better code readability
pygments_style = "friendly"
pygments_dark_style = "native"
highlight_language = "python"

# Additional UI tweaks
html_css_files = [
    "custom.css",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
