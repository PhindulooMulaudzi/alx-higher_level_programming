#!/usr/bin/python3
"""Student Module."""


class Student:
    """Student model."""

    def __init__(self, first_name, last_name, age):
        """Initialize method."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get representation of student instance."""
        return vars(self)
