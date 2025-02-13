#!/usr/bin/python3
"""
Module for reading and printing a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    :param filename: Name of the file to read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
