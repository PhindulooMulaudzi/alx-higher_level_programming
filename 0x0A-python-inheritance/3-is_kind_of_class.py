#!/usr/bin/python3
"""class and class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if object is instance or inherited instance of a class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj.
    Returns:
        If obj is an instance or inherited instance.
    """
    if isinstance(obj, a_class):
        return True
    return False
