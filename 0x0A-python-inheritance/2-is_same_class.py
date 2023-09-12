#!/usr/bin/python3
"""
Module to check class
"""


def is_same_class(obj, a_class):
    """check  if same type of object
    args:
        obj: the object
        a_class: class type
    Return:
        True or False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
