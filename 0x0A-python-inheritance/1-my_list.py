#!/usr/bin/python3
"""contains the MyList class."""


class MyList(list):
    """subclass of list."""

    def __init__(self):
        """Initialize the object."""
        super().__init__()

    def print_sorted(self):
        """Print sorted list."""
        print(sorted(self))
