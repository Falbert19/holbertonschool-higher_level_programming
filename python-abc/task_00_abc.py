#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def sound(self):
        pass


class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")

dog = Dog()
dog.sound     ()
cat = Cat()
cat.sound
