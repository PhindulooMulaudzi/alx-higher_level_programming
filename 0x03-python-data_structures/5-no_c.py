#!/usr/bin/python3
def no_c(my_string):
    result = my_string.translate({ord(char): "" for char in 'Cc'})
    return result
