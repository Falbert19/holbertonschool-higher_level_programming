#!/usr/bin/python3
"""
Divides all elements of a matrix by a given divisor

arguments: matrix is a list of a list were
each element is a int or a float

Raises:
        TypeError: If the matrix is not a list of lists of integers or floats
        TypeError: If the rows of the matrix are not all the same size
        TypeError: If the divisor is not a number
        ZeroDivisionError: If the divisor is zero

Returns: a new matrix

"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
