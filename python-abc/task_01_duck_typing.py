#!/usr/bin/env python3
"""
Module defining an abstract base class Shape and its
concrete subclasses Circle and Rectangle.
Also includes a function for handling
shape information using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of a shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of a shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle, inheriting from Shape.
    """

    def __init__(self, radius: float):
        """
        Initializes the Circle with a given radius.

        Args:
            radius (float): The radius of the circle.

        Raises:
            ValueError: If the radius is negative.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self) -> float:
        """
        Returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """
        Returns the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle, inheriting from Shape.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes the Rectangle with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.

        Raises:
            ValueError: If width or height is negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape: Shape):
    """
    Prints the area and perimeter of a given shape
    using duck typing.

    Args:
        shape (Shape): An object that implements area()
        and perimeter() methods.
    """
    print(f"Area: {shape.area():.5f}")
    print(f"Perimeter: {shape.perimeter():.5f}")
