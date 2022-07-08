#!/usr/bin/python3
""" A module containing a single class
    Class:
        -Base
"""
import json


class Base:
    """ Base class containing the constructor """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries=[]):
        """Json representation of list_dictionaries"""
        if(list_dictionaries == [] or list_dictionaries is None):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
