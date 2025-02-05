import os
import fortran77punchcards


def test_open_image():
    fortran77punchcards.punch.card()


def test_line():
    i = fortran77punchcards.punch.make_line(
        "      PRINT *,'Hello World'")

    i.save(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "output_test_line.png"
    ))

