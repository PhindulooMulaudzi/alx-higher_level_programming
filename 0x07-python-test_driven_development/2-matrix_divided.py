#!/usr/bin/python3
"""Module for matrix division."""


def matrix_divided(matrix, div):
    """Divide elemments of a matrix.

    Args:
        matrix: list of lists of numbers (float/int).
        div: the divisor.
    Raises:
        TypeError: when matrix contains invalid numbers.
        TypeError: matrix are of different sizes.
        TypeError: when divisor is not a number.
        ZeroDivisionError: If division by 0.
    Returns:
        The resultant matrix after division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                    for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a list of lists and "
                        "contain numbers (float / int)")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Matrix must have same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("Divisor must be a number")

    if div == 0:
        raise ZeroDivisionError("Division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
