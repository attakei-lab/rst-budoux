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


@pytest.mark.sphinx("html", confoverrides={"budoux_separator": "<wbr>"})
def test_change_separator(app: SphinxTestApp):
    """Test that it passes with rst-budoux extension."""
    app.build()
    html = app.outdir / "ja.html"
    data = html.read_text()
    assert "\u200b" not in data
    assert "<wbr>" in data


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "budoux_additional_style": "body {word-break: keep-all; overflow-wrap: anywhere;}"  # noqa: E501
    },
)
def test_append_style(app: SphinxTestApp):
    """Test that it passes with rst-budoux extension."""
    app.build()
    html = app.outdir / "ja.html"
    data = html.read_text()
    assert "<style>" in data
    assert app.config.budoux_additional_style in data
