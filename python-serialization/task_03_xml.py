#!/usr/bin/env python3
"""
This module provides functions for
serializing and deserializing Python
dictionaries to and from XML format.

Functions:
- serialize_to_xml(dictionary, filename):
Serializes a Python dictionary into an XML file.
- deserialize_from_xml(filename): Deserializes
an XML file back into a Python dictionary.

Usage:
- serialize_to_xml(): Converts a given
dictionary into an XML file where each dictionary
key is a tag and the corresponding value is the text content.
- deserialize_from_xml(): Parses the XML
file, reconstructing the original dictionary from its tags and values.

XML Format:
- The root element is <data>.
- Each dictionary item is represented as a
child element with the key as the tag and the
value as the element's text content.

Example:
    sample_dict = {'name': 'John', 'age': '28', 'city': 'New York'}
    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    deserialized_data = deserialize_from_xml(xml_file)

This module is part of the task_03_xml.py
file in the Python-serialization project.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Parameters:
    - dictionary (dict): The dictionary to serialize.
    - filename (str): The file to save the serialized XML data.

    Creates an XML file with a root element
    <data> and each key-value pair in the dictionary
    as child elements.
    """
    # Create the root element
    root = ET.Element('data')

    # Iterate over the dictionary and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create an ElementTree object and write the XML to the file
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Parameters:
    - filename (str): The XML file to deserialize.

    Returns:
    - dict: A dictionary reconstructed from the XML data.

    The XML file must have a root element
    <data> with child elements where the tag is the key
    and the text content is the value.
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct the dictionary
    data_dict = {}
    for child in root:
        data_dict[child.tag] = child.text

    return data_dict


if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
