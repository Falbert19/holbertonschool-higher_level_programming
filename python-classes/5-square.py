#!/usr/bin/python3
"""
this module defines a Square class with a validated size, area calculation and
a getter and setter and prints it
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
        self.size = size

    @property
    def size(self):
        """retrieves the size

        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets size

        args:
            value (int): new size of square

        Raises:
        TypeError: if value is not a integer
        ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        computes and return a square area

        Returns:
        int: area of square (size * size)
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square using '#'

        if size is 0, prints an empty line
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
