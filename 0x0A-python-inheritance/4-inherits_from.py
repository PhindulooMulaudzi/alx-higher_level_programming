#!/usr/bin/python3
"""Inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if object is inherited instance.

    Args:
        obj (any): The object.
        a_class (type): The class to match.
    Returns:
        If obj is an inherited instance of or not.
    """
    if issubclass(type(obj), a_class) and not type(obj).isinstance(a_class):
        return True
    return False
