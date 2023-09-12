#!/usr/bin/python3
"""Json to string module."""

import json


def to_json_string(my_obj):
    """Get Json as string.

    args:
        my_obj: object.
    return:
        json.
    """
    return json.dumps(my_obj)
