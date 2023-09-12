#!/usr/bin/python3
"""Rectangle Module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass."""

    def __init__(self, width, height):
        """Construct method."""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute area."""
        return self.__width * self.__height

    def __str__(self):
        """Print method."""
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)
