#!/usr/bin/env python
"""Generate image of working for README."""

from pathlib import Path

import budoux
from docutils import nodes
from docutils.core import publish_doctree, publish_from_doctree
from rst_budoux import parse_all_sentences
from rst_budoux.cli.html import CustomHTMLWriter

ROOT = Path(__file__).parent.parent
SOURCE = "`あなた <http://example.com>`_ に寄り添う **最先端** のテクノロジー。"


def get_env_dir() -> Path:  # noqa: D103
    var = ROOT / "var"
    var.mkdir(parents=True, exist_ok=True)
    return var


def cleanup_document(document: nodes.document) -> nodes.document:
    """Remove single space due to syntax of reStructuredText.

    This proc is to make HTML as similar to original of BudouX as possible.
    """
    all_text: list[nodes.Text] = list(document.findall(nodes.Text))
    for text in all_text:
        content = text.astext()
        if not (content.startswith(" ") or content.endswith(" ")):
            continue
        new_text = nodes.Text(content.strip())
        text.parent.insert(text.parent.index(text), new_text)
        new_text.parent.remove(text)
    return document


def main():  # noqa: D103
    env_dir = get_env_dir()
    # Generate HTML
    document = cleanup_document(publish_doctree(SOURCE))
    with (env_dir / "without-budoux.html").open("w") as fp:
        fp.write(publish_from_doctree(document, writer_name="html5").decode("utf-8"))
    budoux_parser = budoux.load_default_japanese_parser()
    document = parse_all_sentences(budoux_parser, document)
    with (env_dir / "with-budoux.html").open("w") as fp:
        fp.write(
            publish_from_doctree(document, writer=CustomHTMLWriter()).decode("utf-8")
        )


if __name__ == "__main__":
    main()
