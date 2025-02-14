#!/usr/bin/python3
"""
Module: to_json_string

This module contains a function that returns the JSON representation
of an object as a string.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    :param my_obj: The object to serialize.
    :return: JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
