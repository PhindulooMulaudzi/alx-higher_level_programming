#!/usr/bin/python3

"""Square class implimentation."""


class Square:
    """Models a square with a size.

    Attributes
    ----------
    size : int
        The size of the square.
    """

    def __init__(self, size=0):
        """Square class constructor.

        Parameters
        ----------
            size : int
                The size of the new square.

        Raises
        ------
        TypeError
            If the wrong type is passed in for the size.
        ValueError
            If the size of the square is a negative number.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("The size cannot be negative")
        self.__size = size
