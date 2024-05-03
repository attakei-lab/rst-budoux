#!/usr/bin/env python
"""Generate image of working for README."""

from pathlib import Path

import budoux
from docutils import nodes
from docutils.core import publish_doctree, publish_from_doctree
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
from rst_budoux import parse_all_sentences
from rst_budoux.cli.html import CustomHTMLWriter

HERE = Path(__file__).parent
ROOT = HERE.parent


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
        trimmed = content.strip()
        if content == trimmed:
            continue
        new_text = nodes.Text(trimmed)
        text.parent.insert(text.parent.index(text), new_text)
        new_text.parent.remove(text)
    return document


def main():  # noqa: D103
    env_dir = get_env_dir()
    # Generate HTML
    document = cleanup_document(
        publish_doctree(source=(HERE / "example-rst.txt").read_text())
    )
    with (env_dir / "without-budoux.html").open("w") as fp:
        fp.write(
            publish_from_doctree(
                document,
                writer_name="html5",
                settings_overrides={
                    "template": str(HERE / "template.txt"),
                },
            ).decode("utf-8")
        )
    budoux_parser = budoux.load_default_japanese_parser()
    document = parse_all_sentences(budoux_parser, document)
    with (env_dir / "with-budoux.html").open("w") as fp:
        fp.write(
            publish_from_doctree(
                document,
                writer=CustomHTMLWriter(),
                settings_overrides={
                    "template": str(HERE / "template.txt"),
                },
            ).decode("utf-8")
        )
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 528, "height": 220})
        page.goto(f"file://{HERE / 'example-rst.txt'}")
        page.locator("pre").evaluate("e => e.style.fontSize = '32px'")
        page.screenshot(path=env_dir / "source.png")
        page.set_viewport_size({"width": 374, "height": 220})
        page.goto(f"file://{env_dir / 'without-budoux.html'}")
        page.screenshot(path=env_dir / "without-budoux.png")
        page.goto(f"file://{env_dir / 'with-budoux.html'}")
        page.screenshot(path=env_dir / "with-budoux.png")
    # Combine image
    font = ImageFont.truetype("NotoSansCJK-Regular.ttc", 40)
    img = Image.new("RGBA", size=[880, 660], color=(255, 237, 179, 180))
    img_source = Image.open(env_dir / "source.png")
    img.paste(Image.new("RGB", size=[550, 242], color="blue"), (143, 385))
    img.paste(img_source, (154, 396))
    img_with = Image.open(env_dir / "with-budoux.png")
    img.paste(Image.new("RGB", size=[396, 242], color="green"), (451, 33))
    img.paste(img_with, (462, 44))
    text_with = ImageDraw.Draw(img)
    text_with.text((462, 286), "↑ with rst-budoux", "black", font=font)
    img_without = Image.open(env_dir / "without-budoux.png")
    img.paste(Image.new("RGB", size=[396, 242], color="green"), (33, 33))
    img.paste(img_without, (44, 44))
    text_without = ImageDraw.Draw(img)
    text_without.text((110, 286), "docutils only ↑", "black", font=font)
    with (ROOT / "mv.png").open("wb") as fp:
        img.save(fp, "PNG")


if __name__ == "__main__":
    main()
