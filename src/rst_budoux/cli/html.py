"""Entrypoint module for ``rst-budoux2html``."""

import argparse
from pathlib import Path

import budoux
from docutils import frontend
from docutils.core import publish_doctree, publish_from_doctree
from docutils.writers import html5_polyglot

from .. import parse_all_sentences
from ..writers import depart_word_break
from ..writers.html import DEFAULT_SEPARATOR, visit_word_break

parser = argparse.ArgumentParser()
parser.add_argument("src", type=Path)
parser.add_argument("--budoux-separator", default=DEFAULT_SEPARATOR)


class CustomHTMLWriter(html5_polyglot.Writer):  # noqa: D101
    settings_spec = frontend.filter_settings_spec(
        html5_polyglot.Writer.settings_spec,
        budoux_separator=(
            "Separation text using on <word-break> node",
            ["--budoux-separator"],
            {"default": DEFAULT_SEPARATOR},
        ),
    )

    def __init__(self):  # noqa: D107
        super().__init__()
        self.translator_class = CustomHTMLTranslator


class CustomHTMLTranslator(html5_polyglot.HTMLTranslator):  # noqa: D101
    visit_WordBreak = visit_word_break
    depart_WordBreak = depart_word_break


def main():  # noqa: D103
    args = parser.parse_args()
    document = publish_doctree(args.src.read_text())
    budoux_parser = budoux.load_default_japanese_parser()
    document = parse_all_sentences(budoux_parser, document)
    print(
        publish_from_doctree(
            document,
            writer=CustomHTMLWriter(),
            settings_overrides={"budoux_separator": args.budoux_separator},
        ).decode("utf-8")
    )
