#!/usr/bin/python3
"""Json module."""


def class_to_json(obj):
    """Get dict from object.

    args:
        obj: object
    return:
        serialized object
    """
    return vars(obj)
