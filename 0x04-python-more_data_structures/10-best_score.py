#!/usr/bin/python3


def best_max_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        max_score = 0
        max_key = ""
        for i in my_list:
            if a_dictionary[i] > max_score:
                max_score = a_dictionary[i]
                max_key = i
        return max_key
