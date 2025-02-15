#!/usr/bin/python3
"""
Module: load_from_json_file

This module contains a function that creates a
Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    :param filename: The name of the JSON file to read from
    :return: Corresponding Python object
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
