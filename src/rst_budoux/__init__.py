import budoux
from docutils import nodes


class WordBreak(nodes.Element):
    tagname = "word-break"


def parse_all_sentences(
    parser: budoux.Parser, document: nodes.document
) -> nodes.document:
    all_text = list(document.findall(nodes.Text))
    for node in all_text:
        parent = node.parent
        tokens = parser.parse(str(node))
        children = []
        for token in tokens:
            children.append(nodes.Text(token))
            children.append(WordBreak())
        children.pop()
        parent.remove(node)
        for child in children:
            parent.append(child)
    return document
