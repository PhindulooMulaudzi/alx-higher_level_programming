#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list: list to print elements from.
        x: number of elements in my_list to print.

    Returns:
        number of elements printed.
    """
    ret_val = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret_val += 1
        except IndexError:
            break
    print("")
    return (ret_val)
