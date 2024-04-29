"""Extend functions for html writer classes."""

from docutils.writers._html_base import HTMLTranslator

from .. import WordBreak


def visit_word_break(self: HTMLTranslator, node: WordBreak):
    """Write a tag when visit on <word-break>."""
    self.body.append("<wbr>")


def depart_word_break(self: HTMLTranslator, node: WordBreak):
    """When depart from <word-break>, translator do nothing."""
    pass
