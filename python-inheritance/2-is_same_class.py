#!/usr/bin/python3
"""
returns True if the object is exactly an
instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is an instance of the specified class
    Otherwise, returns False

    Args:
        obj: object to check
        a_class: class to compare against

    Returns:
        bool: True if obj is exactly an instance of a_class,
        otherwise False """
    return type(obj) is a_class
