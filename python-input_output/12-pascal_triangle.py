#!/usr/bin/python3
"""
Module: pascal_triangle

This module contains a function that
generates Pascal's Triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.

    :param n: Number of rows in Pascal's triangle.
    :return: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
