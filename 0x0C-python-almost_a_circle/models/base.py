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
            with open(filename, "w", newline="\n") as f:
                f.write(json_repr)

    @staticmethod
    def from_json_string(json_string):
        """Creating list of dictionary from json string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an object from dictionary"""
        obj = cls()
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        obj_list = []
        try:
            f = open(filename, 'r')
            json_string = f.read()
            obj_dict_list = cls.from_json_string(json_string)
            for obj_dict in obj_dict_list:
                obj_list.append(cls.create(**obj_dict))
            return obj_list
        except FileNotFoundError as fe:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objs to csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                obj_dict = obj._to_dictionary()
                for key in obj_dict:
                    f.write("{:s}, {:d}".format(key, obj_dict[key]))

    @classmethod
    def load_from_file_csv(cls):
        """Load csv to obj"""
