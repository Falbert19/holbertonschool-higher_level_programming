#!/usr/bin/env python3
"""
Module defining VerboseList, a subclass of
list that provides notifications for modifications.
"""


class VerboseList(list):
    """
    A custom list subclass that prints
    notifications whenever items are added or removed.
    """

    def append(self, item):
        """
        Adds an item to the list and prints a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list with multiple items and prints a notification.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a notification.
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """
        Removes and returns an item at
        the given index and prints a notification.
        """
        if len(self) == 0:
            print("Cannot pop from an empty list.")
            return None
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
