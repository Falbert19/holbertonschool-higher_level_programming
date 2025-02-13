#!/usr/bin/python3
"""
Module for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written.

    This function ensures that:
    - The file is created if it does not exist.
    - The content of the file is overwritten if it already exists.
    - The number of characters written is returned.

    :param filename: Name of the file to write to.
    :param text: The text to write into the file.
    :return: Number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
