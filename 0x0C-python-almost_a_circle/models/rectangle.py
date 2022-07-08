#!/usr/bin/python3
""" A module containing a single class
    Class:
        -Rectangle
"""
from .base import Base


class Rectangle(Base):
    """ Rectangle class, containing constructor, getters and setters """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self._all_attrs = ["id", "_width", "_height", "_x", "_y"]

    @property
    def width(self):
        """ width getter """
        return self._width

    @width.setter
    def width(self, width):
        """ width setter """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self._width = width

    @property
    def height(self):
        """ height getter """
        return self._height

    @height.setter
    def height(self, height):
        """ height setter """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self._height = height

    @property
    def x(self):
        """ x getter """
        return self._x

    @x.setter
    def x(self, x):
        """ x setter """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self._x = x

    @property
    def y(self):
        """ y getter """
        return self._y

    @y.setter
    def y(self, y):
        """ y setter """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self._y = y

    def area(self):
        """ Area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Display the rectangle with # character """
        for yy in range(self.y):
            print("")
        for h in range(self.height):
            for xx in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print('#', end="")
            print("")

    def __str__(self):
        """ Overring/Customizing print (verbose) function """
        desc = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return desc.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update attributes values)
            Args:
                -id: The identifier of the object
                -width: The width of the rectangle
                -height: The height of the rectangle
                -x: The x coordinate of the rectangle
        """ 
        if len(args) > 0:
            idx = 0
            while idx < len(args):
                # self.__dict__[all_attrs[idx]] = args[idx]
                setattr(self, self._all_attrs[idx], args[idx])
                idx += 1
        else:
            for key, value in kwargs.items():
                if key != "id":
                    if key == "size":
                        key = "width"
                    real_key = "_" + key
                else:
                    real_key = key
                idx = self._all_attrs.index(real_key)
                setattr(self, self._all_attrs[idx], value)

    def to_dictionary(self):
        self_dict = {}
        attrs_to_see = ["x", "y", "id", "height", "width"]
        for key, value in self.__dict__.items():
            if key != "_all_attrs":
                attr = key.replace('_', '')
                self_dict[attr] = self.__dict__.get(key)
        return self_dict
