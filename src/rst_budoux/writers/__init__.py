# noqa: D104
from docutils import nodes

from .. import WordBreak


def depart_word_break(self: nodes.NodeVisitor, node: WordBreak):
    """When depart from <word-break>, translator do nothing."""
    pass
