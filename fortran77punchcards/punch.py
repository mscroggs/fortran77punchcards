"""Punchcards."""

import os
import typing
from PIL import Image
from fortran77punchcards.character_encoding import encoding

_card = None


def card() -> Image.Image:
    """Get image of punchcard."""
    global _card
    if _card is None:
        _card = Image.open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), "punchcard.png")
        ).convert("RGBA")
    return _card.copy()


def make_line(line: str) -> Image.Image:
    """Convert a line of FORTRAN77 to an image of a punchcard."""
    img = card()

    for col, c in enumerate(line.upper()):
        if c not in encoding:
            raise ValueError(f"Invalid character: {c}")
        for row in encoding[c]:
            x0 = int(95 + 35.2 * col)
            if row == 11:
                y0 = 175
            elif row == 12:
                y0 = 75
            else:
                y0 = 275 + 100 * row
            img.paste((255, 255, 255, 0), (x0, y0, x0 + 29, y0 + 80))

    return img


def make_script(lines: typing.List[str], width: int = 2000, row_size: int = 100) -> Image.Image:
    """Convert a FORTRAN77 script to images of punchcards."""
    lines = [i for i in lines if i != ""]
    c = card()
    height = int(width * c.size[1] / c.size[0])
    padding = int(0.05 * height)

    rows = min(len(lines), row_size)
    cols = 1 + (len(lines) - 1) // row_size
    image_height = int(height * rows + padding * (rows - 1))
    image_width = int(width * cols + padding * (cols - 1))

    img = Image.new(mode="RGBA", size=(image_width, image_height))

    for i, line in enumerate(lines):
        c = make_line(line).resize((width, height))
        img.paste(
            c, (int((width + padding) * (i // row_size)), int((height + padding) * (i % row_size)))
        )

    return img
