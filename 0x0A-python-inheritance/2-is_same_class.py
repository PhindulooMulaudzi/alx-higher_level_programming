#!/usr/bin/python3
"""Class-checking function."""


def is_same_class(obj, a_class):
    """Check if object is instance of a class.

    Args:
        obj (any): The object.
        a_class (type): The class to match.
    Returns:
        If obj is exactly an instance of a_class.
    """
    if type(obj).isinstance(a_class):
        return True
    return False
