"""Convert a FORTRAN77 script into a picture of a set of punchcards."""

import argparse

from fortran77punchcards.punch import make_script

parser = argparse.ArgumentParser(description="Generate files from templates in a directory")
parser.add_argument(
    "input_file", metavar="input_file", nargs=1, default=None, help="FORTRAN file (input)"
)
parser.add_argument(
    "output_file", metavar="output_file", nargs=1, default=None, help="PNG (output)"
)
parser.add_argument(
    "--width", metavar="width", nargs="?", default=2000, help="Width in pixels of output image"
)
parser.add_argument(
    "--row-size",
    metavar="row_size",
    nargs="?",
    default=15,
    help="The number of cards in each column",
)
args = parser.parse_args()

input_file = args.input_file[0]
output_file = args.output_file[0]
width = int(args.width)
row_size = int(args.row_size)

assert output_file.endswith(".png")

with open(input_file) as f:
    lines = f.read().split("\n")

img = make_script(lines, width=width, row_size=row_size)
img.save(output_file)
