#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list
    """
    unique_list = []
    sum = 0
    for num in my_list:
        if num not in unique_list:
            sum += num
            unique_list.append(num)
    return sum
