#!/usr/bin/python3
"""
    Writes a string to a text file (UTF8)
    and returns the number of characters written.

    :param filename: Name of the file to write to.
    :param text: The text to write into the file.
    :return: Number of characters written.
"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
