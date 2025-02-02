#!/usr/bin/python3
"""this module will define a Rectangle empty"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """
        initializes a new rectangle instance

        Args:
            width (int): width of rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrives th width of rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle

        Args:
            value (int): new width value

        Raises
            TypeError: height must be an integer
            ValueError: width must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        retrieves the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
