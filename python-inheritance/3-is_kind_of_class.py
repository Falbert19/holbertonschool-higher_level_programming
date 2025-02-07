#!/usr/bin/python3
"""returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False """


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    Args:
        obj: object to check
        a_class: class to compare

    Returns:
        bool: True if obj is an instance
        of a_class or its subclass, otherwise False
    """
    return isinstance(obj, a_class)
