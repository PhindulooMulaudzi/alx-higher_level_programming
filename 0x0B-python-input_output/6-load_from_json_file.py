#!/usr/bin/python3
"""Create object module."""

import json


def load_from_json_file(filename):
    """Create json object.

    args:
        filename: file.
    return:
        object.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
