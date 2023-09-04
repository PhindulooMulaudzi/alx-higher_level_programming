#!/usr/bin/python3
"""Module for printing a square to console."""


def print_square(size):
    """Print a square using # character.

    Args:
        size: the width and height of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: when the size is negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be a positive number")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
