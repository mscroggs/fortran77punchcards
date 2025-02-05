# FORTRAN77 Punchcards

`fortran77punchcards` is a Python library that converts FORTRAN77 code to images of punchcards.

The code is licensed under a [MIT license](LICENSE). The [image of a punchcard]() is licensed
under a [CC BY 4.0 license](LICENSE-CC).

## Installing

This library can be installed by running:

```bash
pip install fortran77punchcards
```

## Usage

A script called `program.f` can be converted into the image `program.png` with a width
of 1000 pixels by running:

python -m fortran77punchcards program.f program.png --width 1000
