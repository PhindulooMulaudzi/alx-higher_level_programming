#!/usr/bin/python3
"""Write to file module."""


def write_file(filename="", text=""):
    """Write to file.

    args:
        filename: file
    text:
        text: text to write
    return:
        number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
