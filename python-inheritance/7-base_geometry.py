#!/usr/bin/python3
"""
instance method: def area(self): that raises Exception, ValueError or TypeError
"""


class BaseGeometry:
    """class that raise a exception ValueError, or TypeError"""
    def area(self):
        """ Raises Exception message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer

        Args:
            name (str): name of variable
            value (int): value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
