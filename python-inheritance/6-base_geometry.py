#!/usr/bin/python3
"""
instance method: def area(self): that raises an
Exception with the message area() is not implemented
"""


class BaseGeometry:
    """class that raise a exception"""
    def area(self):
        """ Raises Exception message area() is not implemented """
        raise Exception("area() is not implemented")
