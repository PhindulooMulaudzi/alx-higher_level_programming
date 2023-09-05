#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Return the sumation of a and b.

    Float arguments will be casted to integers

    Raises:
        TypeError: If any of the arguments is not a number
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
