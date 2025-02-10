#!/usr/bin/env python3
"""
Module defining Fish, Bird, and FlyingFish
classes to demonstrate multiple inheritance.
"""


class Fish:
    """
    Class representing a Fish with swimming ability and water habitat.
    """

    def swim(self):
        """
        Prints a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message about the fish's habitat.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a Bird with flying ability and sky habitat.
    """

    def fly(self):
        """
        Prints a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message about the bird's habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish, which can both swim and fly.
    Inherits from both Fish and Bird.
    """

    def fly(self):
        """
        Overrides the fly method to describe the flying fish's ability.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Overrides the swim method to describe the flying fish's swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Overrides the habitat method to
        describe the flying fish's dual habitat
        """
        print("The flying fish lives both in water and the sky!")
