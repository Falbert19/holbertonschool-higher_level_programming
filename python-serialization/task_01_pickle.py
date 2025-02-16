#!/usr/bin/env python3
"""
Serialization and deserialization using the
pickle module for a custom Python object.
"""

import pickle


class CustomObject:
    """
    A custom class representing a simple object with
    serialization and deserialization capabilities.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        (f"Name: {self.name}\nAge: {self.age}\n"
         f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.

        Args:
            filename (str): The filename to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file.

        Args:
            filename (str): The filename to load the serialized object from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
