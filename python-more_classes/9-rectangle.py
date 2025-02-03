#!/usr/bin/python3
"""defines a class Rectangle with methods,
include a class method creating a square
"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        number_of_instance (int): number of rectangle instance
        print_symbol (any): symbol used for string rep
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes a new Rectangle instance

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle

        Args:
            value (int): new width value

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): The new height value

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates and returns the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates and returns the perimeter of the rectangle

        Returns:
            int: the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return the string representation of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        lines = []
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """returns the official string
        representation of the rectangle
         """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when a instance
        of rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the greater or equal area

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError: if rect_1 is not an instance of Rectangle
            TypeError: if rect_2 is not an instance of Rectangle

        Returns:
            Rectangle: rect_1 if its area is greater
            than or equal to rect_2's area,
                       otherwise rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        return a new rectangle instance where width
        and height are equal

        Args:
            size (int): size of square

        Returns:
            rectangle: new rectangle isntance with == sides
        """
        return cls(size, size)
