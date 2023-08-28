#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print first x elements of a list that are integers.

    Args:
        my_list: The list to print elements from.
        x: number of elements in my_list to print.

    returns:
        The number of elements printed.
    """
    ret_val = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret_val += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret_val)
