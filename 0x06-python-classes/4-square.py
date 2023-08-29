#!/usr/bin/python3

"""Square class implimentation."""


class Square:
    """Models a square with a size.

    Attributes
    ----------
    size : int
        The size of the square.

    Methods
    -------
    area()
        Returns the area of the square instance.
    size()
        Return the size of the current square instance.
    """

    def __init__(self, size=0):
        """Square class constructor.

        Parameters
        ----------
            size : int
                The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for the square class.

        Parameters
        ----------
            value : int
                The size of the square

        Raises
        ------
        TypeError
            If the wrong type is passed in for the size.
        ValueError
            If the size of the square is a negative number.

        Return
        ------
            None
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("The size cannot be negative")
        self.__size = value

    def area(self):
        """
        Define the area of the square.

        Parameters
        ----------
            None

        Return
        ------
            Area of the square
        """
        return (self.__size * self.__size)
