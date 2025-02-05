import os
import fortran77punchcards

path = os.path.dirname(os.path.realpath(__file__))


def test_open_image():
    fortran77punchcards.punch.card()


def test_line():
    i = fortran77punchcards.punch.make_line("      PRINT *,'Hello World'")

    i.save(os.path.join(path, "output_test_line.png"))


def test_script():
    i = fortran77punchcards.punch.make_script(
        [
            "c  this line is a comment",
            "c  comments are a waste of punchcards",
            "      PRINT *,'Hello World'",
        ]
    )

    i.save(os.path.join(path, "output_test_script.png"))
