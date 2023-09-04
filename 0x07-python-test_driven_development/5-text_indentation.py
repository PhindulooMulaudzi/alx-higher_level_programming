#!/usr/bin/python3
"""Module for indenting text."""


def text_indentation(text):
    """Print text with two new line after '.', '?', and ':'.

    Args:
        text: The text to be printed.
    Raises:
        TypeError: If the argument 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
