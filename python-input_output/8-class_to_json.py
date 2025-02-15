#!/usr/bin/python3
"""
Module: class_to_json

This module contains a function that
returns the dictionary description
with simple data structures
(list, dictionary, string, integer, and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structures
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    :param obj: Instance of a class.
    :return: Dictionary representation of the object's attributes.
    """
    return obj.__dict__
