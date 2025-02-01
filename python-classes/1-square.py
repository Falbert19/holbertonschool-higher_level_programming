#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    represents a square

    attributes:
        __size (int): size of the square, private
    """

    def __init__(self, size):
        """
        initializes a Square

        Args:
            size (int): sizes of square
        """
        self.__size = size
