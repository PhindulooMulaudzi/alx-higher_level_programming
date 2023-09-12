#!/usr/bin/python3
"""Read method module."""


def read_lines(filename="", nb_lines=0):
    """Read N lines from text file.

    args:
        filename: file.
        nb_lines: number of lines.
    return:
        void.
    """
    line_num = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line_num < nb_lines or not nb_lines or nb_lines < 0:
                print(line, end="")
            line_num += 1
