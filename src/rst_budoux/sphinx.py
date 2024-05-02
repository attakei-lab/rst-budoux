"""Implementation as Sphinx-extension."""

import budoux
from docutils.writers._html_base import HTMLTranslator
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.docutils import nodes

from . import WordBreak, __version__, parse_all_sentences
from .writers import html


def _configure_visitor(app: Sphinx, config: Config):
    def _visit_word_break(self: HTMLTranslator, node: WordBreak):
        self.body.append(config.budoux_separator)

    app.add_node(WordBreak, html=(_visit_word_break, html.depart_word_break))


def _insert_word_break(app: Sphinx, doctree: nodes.document) -> nodes.document:
    parser = budoux.load_default_japanese_parser()
    return parse_all_sentences(parser, doctree)


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("budoux_separator", "\u200b", "env")
    app.connect("config-inited", _configure_visitor)
    app.connect("doctree-read", _insert_word_break)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
