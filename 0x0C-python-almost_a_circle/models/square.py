#!/usr/bin/python3
"""
Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Init method
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Init method
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Print string with str
        """
        return "[Square] " + "(" + str(self.id) + ") "\
            + str(self.x) + "/" + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """
        Getter: size
        """
        return self.width

    @size.setter
    def size(self, width):
        """
        Setter: size
        """
        self.width = width
        self.height = width

    def update(self, *args, **kwargs):
        """
        Args Update
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Dict representation of class
        """
        dict_attr = {}
        attributes = ['id', 'size', 'x', 'y']
        for key in attributes:
            dict_attr.update({key: getattr(self, key)})
        return dict_attr
