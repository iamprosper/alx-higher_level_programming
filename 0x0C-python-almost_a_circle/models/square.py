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
        """The size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """The size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updating the square"""
        atrs_list = ["id", "size", "x", "y"]
        s_atr = "_Rectangle__{:s}"
        if len(args) > 0:
            idx = 0
            while idx < len(args):
                if idx == 0:
                    setattr(self, "id", args[idx])
                elif idx == 1:
                    self.width = args[idx]
                    self.height = args[idx]
                else:
                    atr = s_atr.format(atrs_list[idx])
                    setattr(self, atr, args[idx])
                idx += 1
        else:
            for k, v in kwargs.items():
                atr = s_atr.format(k)
                if k == "size":
                    self.width = v
                    self.height = v
                else:
                    if k == "id":
                        atr = "id"
                    setattr(self, atr, v)
