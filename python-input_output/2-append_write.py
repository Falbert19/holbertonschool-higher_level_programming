#!/usr/bin/python3
"""
Module: append_write

This module contains a function that appends
a string to the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    :param filename: Name of the file to append to.
    :param text: The string to append.
    :return: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
