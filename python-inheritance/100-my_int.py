#!/usr/bin/python3
"""
Module defining MyInt class which inverts == and != operators.
"""


class MyInt(int):
    """A rebellious integer class that inverts equality operators."""

    def __eq__(self, other):
        """Override == to behave like !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != to behave like ==."""
        return super().__eq__(other)
