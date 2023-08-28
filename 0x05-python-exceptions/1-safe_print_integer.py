#!/usr/bin/python3

def safe_print_integer(value):
    """Print integer with "{:d}".format().

    Args:
        value: integer to print.

    Returns:
        False, if TypeError or ValueError
        Else, True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
