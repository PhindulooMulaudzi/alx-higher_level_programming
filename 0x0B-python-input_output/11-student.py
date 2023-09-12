#!/usr/bin/python3
"""Student Module."""


class Student:
    """Student model."""

    def __init__(self, first_name, last_name, age):
        """Initialize method."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get representation of student.

        args:
            attrs: attributes
        return:
            void
        """
        if not attrs:
            return vars(self)

        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})

    def reload_from_json(self, json):
        """Replace attributes.

        args:
            json: object
        return:
            void
        """
        self.__dict__.update(json)
