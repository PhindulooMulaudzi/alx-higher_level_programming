#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for xy in my_list:
        num += xy[0] * xy[1]
        den += xy[1]

    return (num / den)
