#!/usr/bin/python3
""" A module containing a single class:
    Class:
        -Square - Inherit from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ A class describin a square object.
    It contains constructor an modifiers
    """

    def __init__(self, size, x=0, y=0, id=None):
        """The constructor"""
        super().__init__(size, size, x, y, id)
        # self._all_attrs = ["id", "_width", "_x", "_y"]

    def __str__(self):
        """Print the content of the object"""
        desc = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return desc.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the value of square's attributes"""
        all_attrs = ["id", "size", "x", "y"]
        idx = 0
        if len(args) > 0:
            while idx < len(args):
                setattr(self, all_attrs[idx], args[idx])
                idx += 1
        else:
            for k, v in kwargs.items():
                if k == "size":
                    setattr(self, "_width", v)
                    setattr(self, "_heigth", v)
                else:
                    if key != "id":
                        key = '_' + k
                setattr(self, k, v)

    def to_dictionary(self):
        """Dictionary representaion of square"""
        self_dict = {}
        for k, v in self.__dict__.items():
            key = k.replace('_', '')
            if key == "width":
                key = "size"
            if key != "height":
                self_dict[key] = v
        return self_dict
