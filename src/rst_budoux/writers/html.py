"""Extend functions for html writer classes."""

from docutils.writers._html_base import HTMLTranslator

from .. import WordBreak

DEFAULT_SEPARATOR = "\u200b"


def visit_word_break(self: HTMLTranslator, node: WordBreak):
    """Write a tag when visit on <word-break>."""
    separator = (
        self.settings.budoux_separator
        if hasattr(self.settings, "budoux_separator")
        else DEFAULT_SEPARATOR
    )
    self.body.append(separator)
