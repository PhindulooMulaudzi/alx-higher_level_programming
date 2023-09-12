#!/usr/bin/python3
"""Json Module."""

import json


def from_json_string(my_str):
    """Convert str to object.

    args:
        my_str:string
    return:
        json
    """
    return json.loads(my_str)
