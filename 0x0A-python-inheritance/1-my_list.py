#!/usr/bin/python3
"""module for Mylist."""


class MyList(list):
    """MyList class."""

    def print_sorted(self):
        """Print list."""
        print(sorted(self))
