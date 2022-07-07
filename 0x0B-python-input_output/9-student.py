#!/usr/bin/python3
""" A module containing a single class
    Class:
        -Student
"""


class Student:
    """ A class representing a student
        Args:
            -first_name: The first name of the student
            -last_name: The last name of the student
            -age: The age of the student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
