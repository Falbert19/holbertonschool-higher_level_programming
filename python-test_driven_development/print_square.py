#!/usr/bin/python3
"""
This module will contain a function
that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer or if it's a float < 0.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
