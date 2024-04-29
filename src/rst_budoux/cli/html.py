"""Entrypoint module for ``rst-budoux2html``."""

import argparse
from pathlib import Path

import budoux
from docutils.core import publish_doctree, publish_from_doctree
from docutils.writers import html5_polyglot

from .. import parse_all_sentences
from ..writers import html

parser = argparse.ArgumentParser()
parser.add_argument("src", type=Path)


class CustomHTMLWriter(html5_polyglot.Writer):  # noqa: D101
    def __init__(self):  # noqa: D107
        super().__init__()
        self.translator_class = CustomHTMLTranslator


class CustomHTMLTranslator(html5_polyglot.HTMLTranslator):  # noqa: D101
    visit_WordBreak = html.visit_word_break
    depart_WordBreak = html.depart_word_break


def main():  # noqa: D103
    args = parser.parse_args()
    document = publish_doctree(args.src.read_text())
    budoux_parser = budoux.load_default_japanese_parser()
    document = parse_all_sentences(budoux_parser, document)
    print(publish_from_doctree(document, writer=CustomHTMLWriter()).decode("utf-8"))
