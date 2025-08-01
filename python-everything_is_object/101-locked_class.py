#!/usr/bin/python3
"""
    locked_class: class LockedClass
"""


class LockedClass:
    """
        A class that can only have one attribute first_name.
        Attribute:
             first_name (str): name
    """
    __slots__ = ['first_name']
