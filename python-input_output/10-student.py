#!/usr/bin/python3
"""
Module: student

This module defines a Student class with attributes
first name, last name, and age.
It includes a method to retrieve a dictionary
representation of a Student instance,
allowing optional filtering of attributes.
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        :param first_name: First name of the student.
        :param last_name: Last name of the student.
        :param age: Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: List of attribute names to retrieve (optional).
        :return: Dictionary containing specified attributes,
        or all if attrs is None.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        return self.__dict__
