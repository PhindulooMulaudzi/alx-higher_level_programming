#!/usr/bin/python3
"""Adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add attribute to an object.

    Args:
        obj (any): The object.
        att (str): The name of the attribute.
        value (any): The value.
    Raises:
        TypeError: When attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
