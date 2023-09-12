#!/usr/bin/python3
"""Append module."""


def append_write(filename="", text=""):
    """Append file with text.

    args:
        filename: file
        text: text to append
    return:
        number of characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
