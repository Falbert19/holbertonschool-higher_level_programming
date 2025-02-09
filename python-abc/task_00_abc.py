#!/usr/bin/python3
"""
this module defining an abstract base class
Animal and its subclasses Dog and Cat
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an
animal.
    """

    @abstractmethod
    def sound(self):
        """Abstract method to
implemented by
		subclasses to define the
		animal's sound.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a Dog.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a Cat.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
