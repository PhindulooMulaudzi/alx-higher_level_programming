#!/usr/bin/python3

"""Square class implimentation."""


class Square:
    """Models a square.

    Attributes
    ----------
    size : int
        size of the square.
    position : int
        position of the square.
    area : int
        the area of the square.

    Methods
    -------
    size : int
        Gets size of the square.
    position : int
        Gets position of the square.
    area : int
        Returns the area of the square.

    """

    def __init__(self, size):
        """Square class constructor.

        Parameters
        ----------
            size : int
                The size of the new square.
            position : (int, int)
                The position of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Define the size get/set property of the square class.

        Parameters
        ----------
            None

        Return
        ------
           Size of the square.
        """
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

    def my_print(self):
        """
        Print the square to the terminal using '#'.

        Parameters
        ----------
            None

        Return
        ------
            None
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
