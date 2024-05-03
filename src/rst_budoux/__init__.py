# noqa: D104 -- TODO: Write after
import budoux
from docutils import nodes

__version__ = "0.1.0"


class WordBreak(nodes.Element):
    """A node to explicit that breakpoint of sentence."""

    tagname = "word-break"


def parse_all_sentences(
    parser: budoux.Parser, document: nodes.document
) -> nodes.document:
    """Find all text in document, and split by BudouX."""
    all_text = list(document.findall(nodes.Text))
    for node in all_text:
        parent = node.parent
        idx = parent.index(node)
        tokens = parser.parse(str(node))
        children = []
        for token in tokens:
            children.append(nodes.Text(token))
            children.append(WordBreak())
        children.pop()
        parent.remove(node)
        for child in reversed(children):
            parent.insert(idx, child)
    return document
