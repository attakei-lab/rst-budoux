from rst_budoux import __version__

# -- Project information
project = "rst-budoux"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = __version__

# -- General configuration
extensions = [
    "rst_budoux.sphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
    "sphinx_toolbox.confval",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "ja"

# -- Options for HTML output
html_title = f"{project} v{release}"
html_theme = "furo"
html_static_path = ["_static"]

# -- Options for extensions
# - sphinx.ext.intersphinx
intersphinx_mapping = {
    "docutils": ("https://sphinx-docutils.readthedocs.io/en/latest/", None)
}
# - sphinx.ext.todo
todo_include_todos = True  # -- Options for extensions
# - rst_budoux.sphinx
# budoux_separator = "<wbr>"
budoux_additional_style = """
body {
    word-break: keep-all;
    overflow-wrap: anywhere;
}
"""
