# -- Project information
project = "rst-budoux"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = "0.0.0"

# -- General configuration
extensions = ["rst_budoux.sphinx"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "ja"

# -- Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]

# -- Options for extensions
# - rst_budoux.sphinx
# budoux_separator = "<wbr>"
budoux_additional_style = """
body {
    word-break: keep-all;
    overflow-wrap: anywhere;
}
"""
