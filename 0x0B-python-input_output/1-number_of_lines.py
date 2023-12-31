#!/usr/bin/python3
"""Number of lines module."""


def number_of_lines(filename=""):
    """Get lines from file.

    args:
        filename: file.
    return:
        number of lines.
    """
    line_num = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line_num += 1
    return line_num
