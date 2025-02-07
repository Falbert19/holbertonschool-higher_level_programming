#!/usr/bin/python3
""" class MyList that inherits from list"""


class MyList(list):
    """
    subclass of list that includes a method
    to print the list in sorted order
    """
    def print_sorted(self):
        """
        prints the list but sorted in ascending order
        """
        print(sorted(self))
