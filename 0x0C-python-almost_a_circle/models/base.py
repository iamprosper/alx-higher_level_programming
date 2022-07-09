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

    @staticmethod
    def to_json_string(list_dictionaries=[]):
        """Json representation of list_dictionaries"""
        if(list_dictionaries == [] or list_dictionaries is None):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs=[]):
        """Saving a list of object to corresponding file"""
        class_name = cls.__name__
        filename = class_name + ".json"
        objs_to_dictionary_list = []

        if list_objs != []:
            for obj in list_objs:
                objs_to_dictionary_list.append(obj.to_dictionary())
            json_repr = cls.to_json_string(objs_to_dictionary_list)
            with open(filename, "a+", newline="\n") as f:
                f.write(json_repr)

    @staticmethod
    def from_json_string(json_string):
        """Creating list of dictionary from json string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        obj = cls(width=5, height=5)
        obj.update(**dictionary)
        return obj
