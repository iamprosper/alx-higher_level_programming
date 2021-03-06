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
        """The constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Serializer with filters
            Args:
                -attrs: Filters
        """
        obj_values = self.__dict__
        filters = {}
        if attrs:
            for attr in attrs:
                if obj_values.get(attr):
                    filters[attr] = obj_values.get(attr)
        elif attrs != []:
            filters = obj_values

        return filters

    def reload_from_json(self, json):
        for element in json:
            self.__dict__[element] = json.get(element)
