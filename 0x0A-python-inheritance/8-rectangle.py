#!/usr/bin/python3
"""Rectangle that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent rectangle as BaseGeometry."""

    def __init__(self, width, height):
        """Intialize Rectangle.

        Args:
            width (int): The width of Rectangle.
            height (int): The height of Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
