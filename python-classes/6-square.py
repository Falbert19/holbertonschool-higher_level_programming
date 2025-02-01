#!/usr/bin/python3
"""
this module defines a Square class with a validated size,
position attribute, area calculation and
a getter and setter and prints it
"""


class Square:
    """
    represents a Square

    Attributes:
    _size (init): size of square, private
    _position (tuple): position of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Init a Square instance

        args:
        size (int): size of square
        position (tuple): position of square

        Raises:
            TypeError: if size is not a integer
            ValueError: if size is less than 0
            TypeError: if position is not a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrives position of square

        Returns:
            tuple: (x, y)position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets position of square

        args:
            value (tuple): tuple of 2 positive integers

        Raises:
        TypeError: if position is not a tuple of 2 positive integers
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
