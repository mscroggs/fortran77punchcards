import os
from PIL import Image
from PIL import ImageDraw
from fortran77punchcards.character_encoding import encoding

_card = None


def card() -> Image:
    """Get image of punchcard."""
    global _card
    if _card is None:
        _card = Image.open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "punchcard.png"
        )).convert("RGBA")
    return _card.copy()


def make_line(line: str) -> Image:
    """Convert a line of FORTRAN77 to an image of a punchcard."""
    img = card()

    mask = Image.new('L', img.size, color=255)
    draw = ImageDraw.Draw(mask)

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
            img.paste((255, 255, 255, 0), [x0, y0, x0 + 29, y0 + 80])

    return img
