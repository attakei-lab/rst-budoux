from docutils.writers._html_base import HTMLTranslator
from .. import WordBreak


def visit_word_break(self: HTMLTranslator, node: WordBreak):
    self.body.append("<wbr>")


def depart_word_break(self: HTMLTranslator, node: WordBreak):
    pass
