#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by sorted_keys
    """
    sorted_keys = list(a_dictionary.sorted_keys()).sort()
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
