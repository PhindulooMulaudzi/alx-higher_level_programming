#!/usr/bin/python3
"""
module for Mylist
"""


class MyList(list):
    """MyList class
    """

    def print_sorted(self):
        """print list
        """
        print(sorted(self))
