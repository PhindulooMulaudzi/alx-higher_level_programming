#!/usr/bin/python3
"""Base geometry class."""


class BaseGeometry:
    """Model base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter.

        Args:
            name (str): name of parameter.
            value (int): the parameter.
        Raises:
            TypeError: If value not an integer.
            ValueError: If value is <= 0.
        """
        if not type(value).isinstance(int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
