#!/usr/bin/python3
"""
Module: from_json_string

This module contains a function that returns a
Python object from a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    :param my_str: The JSON string to deserialize.
    :return: Corresponding Python object.
    """
    return json.loads(my_str)
