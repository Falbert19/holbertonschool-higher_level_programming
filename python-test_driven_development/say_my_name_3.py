#!/usr/bin/python3
"""
This module is a function `say_my_name` that prints the user's full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>"

    Args:
        first_name (str)
        last_name (str)

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
