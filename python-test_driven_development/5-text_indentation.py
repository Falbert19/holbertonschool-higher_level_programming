#!/usr/bin/python3
"""
this module that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each
    of these characters: ".", "?", and ":"

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in '.?:':
            print(text[i], end='')
            print()
            print()
            i += 1
        elif text[i] == ' ' and (i == 0 or text[i-1] in '.?:'):
            i += 1
        else:
            print(text[i], end='')
            i += 1
