#!/usr/bin/python3
"""MyInt that inherits from int."""


class MyInt(int):
    """Invert operators == and !=."""

    def __eq__(self, value):
        """Override == with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != with == behavior."""
        return self.real == value
