#!/usr/bin/python3
"""Inherits module."""


def inherits_from(obj, a_class):
    """Check if object is instance of class.

    args:
        obj: object
        a_class: class to check
    returns:
        True or False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
