"""Standard tests as Sphinx-extension."""

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp):
    """Test that it passes with rst-budoux extension."""
    app.build()
