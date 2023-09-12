#!/usr/bin/python3
"""Append module."""


def append_after(filename="", search_string="", new_string=""):
    """Append function."""
    result = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            result += line
            if search_string in line:
                result += new_string
    with open(filename, mode="w") as f:
        f.write(result)
