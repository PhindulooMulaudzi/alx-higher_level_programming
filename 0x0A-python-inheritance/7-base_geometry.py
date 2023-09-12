#!/usr/bin/python3
"""BaseGeometry module."""


class BaseGeometry:
    """Geometry class."""

    def area(self):
        """Raise exception when area not implemented."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Check if value is an integer."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))