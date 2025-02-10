#!/usr/bin/python3
"""
Module defining add_attribute function.
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to add an attribute to.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):  # Checks if the object allows dynamic attributes
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)  # Adds the new attribute
