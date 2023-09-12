#!/usr/bin/python3
"""Define square module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherit from Rectangle."""

    def __init__(self, size):
        """Initialise method."""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Print method."""
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__size, self.__size)
