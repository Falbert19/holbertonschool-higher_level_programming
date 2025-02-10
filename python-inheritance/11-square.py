#!/usr/bin/python3
"""
Module defining a Square class
that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square, which is a
    special case of a Rectangle."""

    def __init__(self, size):
        """Initialize size with validation.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
