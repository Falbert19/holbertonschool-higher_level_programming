#!/usr/bin/python3
"""
this returns True if the object is an
instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that
    inherited from the specified class; otherwise, returns False

    Args:
        obj: object to check
        a_class: class to compare

    Returns:
        bool: True if obj is an instance of
        a subclass of a_class, but not a_class itself
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
