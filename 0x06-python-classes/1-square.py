#!/usr/bin/python3

"""Square class implimentation."""


class Square:
    """Models a square with a size.

    Attributes
    ----------
    size : int
        The size of the square.
    """

    def __init__(self, size):
        """Square class constructor.

        Parameters
        ----------
            size : int
                The size of the new square.
        """
        self.__size = size
