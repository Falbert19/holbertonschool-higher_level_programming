#!/usr/bin/env python3
"""
Basic serialization module for saving and
loading Python dictionaries as JSON files.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it into a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
