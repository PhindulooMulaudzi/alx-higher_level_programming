#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Computes the square value
    of all integers in a matrix.
    """
    new_matrix = []
    for col in matrix:
        result = [x**2 for x in col]
        new_matrix.append(result)
    return new_matrix
