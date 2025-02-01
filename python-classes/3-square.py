#!/usr/bin/python3
"""
this module defines a Square class with a validated size and area
"""


class Square:
    """
    represents a Square

    Attributes:
    _size (init): size of square, private
    """

    def __init__(self, size=0):
        """
        Init a Square instance

        args:
        size (int): size of square

        Raises:
            TypeError: if size is not a integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        computes and return a square area

        Returns:
        int: area of square (size * size)
        """
        return self.__size ** 2
