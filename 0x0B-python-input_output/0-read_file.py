#!/usr/bin/python3
"""Read file module."""


def read_file(filename=""):
    """Read a file.

    args:
        filename: file to read
    return:
        void
    """
    with open(filename, encoding="utf-8") as f:
        for line in f.read():
            print(line, end="")
