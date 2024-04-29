import argparse
from pathlib import Path

from docutils.core import publish_doctree, publish_from_doctree

parser = argparse.ArgumentParser()
parser.add_argument("src", type=Path)


def main():
    args = parser.parse_args()
    document = publish_doctree(args.src.read_text())
    # TODO: Pass converter
    print(publish_from_doctree(document, writer_name="pseudoxml").decode("utf-8"))
