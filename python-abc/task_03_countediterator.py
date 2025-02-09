#!/usr/bin/python3
"""
Module defining a CountedIterator class that extends an iterator
to track the number of items iterated over.
"""

class CountedIterator:
    """
    A custom iterator that wraps around an iterable and counts the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.
        
        Args:
            iterable (iterable): The iterable to wrap.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Returns itself as an iterator.
        """
        return self

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the count.

        Returns:
            The next item in the sequence.

        Raises:
            StopIteration: If no more items are left in the iterator.
        """
        item = next(self.iterator)  # Raises StopIteration automatically if exhausted
        self.count += 1
        return item

    def get_count(self):
        """
        Returns the number of items that have been iterated over.
        
        Returns:
            int: The count of iterated items.
        """
        return self.count
