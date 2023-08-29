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

    def __init__(self, size=0, position=(0, 0)):
        """Square class constructor.

        Parameters
        ----------
            size : int
                The size of the new square.
            position : (int, int)
                The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Define the position get/set property of the square class.

        Parameters
        ----------
            None

        Return
        ------
            Position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter method for the position of the square.

        Parameters
        ----------
            value : int
                Position of the the square

        Raises
        ------
        TypeError
            If the wrong type is passed in for the position.

        Return
        ------
            Position of the square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
