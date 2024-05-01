"""Standard tests as Sphinx-extension."""

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp):
    """Test that it passes with rst-budoux extension."""
    app.build()


@pytest.mark.sphinx("html")
def test_parsed_document(app: SphinxTestApp):
    """Test that it passes with rst-budoux extension."""
    app.build()
    html = app.outdir / "ja.html"
    data = html.read_text()
    assert "\u200b" in data
