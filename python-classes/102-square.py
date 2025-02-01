#!/usr/bin/python3
"""
this module defines a Square class with a validated size, area calculation and
comapre methods
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

    def __eq__(self, other):
        """
        check if two squares have the same area
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        check if two squares have different areas
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        check if this square is smaller than another
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        check if this square is smaller than or equal to another
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """check if this square is larger than another
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        check if this square is larger than or equal to another
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
