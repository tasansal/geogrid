"""Sphinx configuration."""
project = "GeoGrid"
author = "Altay Sansal"
copyright = "2022, Altay Sansal"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
