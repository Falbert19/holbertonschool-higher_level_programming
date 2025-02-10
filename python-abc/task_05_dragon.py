#!/usr/bin/env python3
"""
Module defining SwimMixin, FlyMixin, and
Dragon classes to demonstrate mixins.
"""


class SwimMixin:
    """
    Mixin class providing swimming functionality.
    """

    def swim(self):
        """
        Prints a message indicating the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class providing flying functionality.
    """

    def fly(self):
        """
        Prints a message indicating the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class inheriting from SwimMixin and
    FlyMixin to gain swimming and flying abilities.
    """

    def roar(self):
        """
        Prints a message indicating the dragon's roar.
        """
        print("The dragon roars!")
