"""Sphinx configuration."""
project = "LeadLog"
author = "Mark Moreno"
copyright = "2024, Mark Moreno"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
