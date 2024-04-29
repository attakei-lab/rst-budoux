"""Entrypoint module for ``rst-budoux2psuedoxml``."""

import argparse
from pathlib import Path

import budoux
from docutils.core import publish_doctree, publish_from_doctree

from .. import parse_all_sentences

parser = argparse.ArgumentParser()
parser.add_argument("src", type=Path)


def main():  # noqa: D103
    args = parser.parse_args()
    document = publish_doctree(args.src.read_text())
    budoux_parser = budoux.load_default_japanese_parser()
    document = parse_all_sentences(budoux_parser, document)
    print(publish_from_doctree(document, writer_name="pseudoxml").decode("utf-8"))
