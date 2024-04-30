from pathlib import Path
from typing import List

import budoux
import pytest
from docutils.core import publish_doctree, publish_from_doctree

root = Path(__file__).parent


def get_pattern_dirs() -> List[Path]:
    """Return structure of folder-path as test pattern.

    .. note:: This is for parametrize.
    """
    return [p for p in (root / "patterns").glob("*") if p.is_dir()]


@pytest.mark.parametrize("pattern_dir", get_pattern_dirs())
def test_parse_all_sentences(pattern_dir: Path):
    from rst_budoux import parse_all_sentences

    source = pattern_dir / "source.rst"
    expect = pattern_dir / "pseudoxml.txt"
    parser = budoux.load_default_japanese_parser()
    document = publish_doctree(source.read_text())
    document = parse_all_sentences(parser, document)
    result = publish_from_doctree(document, writer_name="pseudoxml").decode("utf-8")
    assert result == expect.read_text()
