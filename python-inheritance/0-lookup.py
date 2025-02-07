#!/usr/bin/python3

def lookup(obj):
    """
    returns the list of available attributes and methods of an object

    Args:
        obj: object to inspect

    Returns:
        List that containing the object's attributes and method
    """
    return dir(obj)
