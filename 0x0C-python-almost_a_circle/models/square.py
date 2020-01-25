#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """
    Print string with str
    """
    def __str__(self):
        return "[Square] " + "(" + str(self.id) + ") "\
            + str(self.x) + "/" + str(self.y) + " - " + str(self.width)

    """
    Getter: size
    """
    @property
    def size(self):
        return self.width

    """
    Setter: size
    """
    @size.setter
    def size(self, width):
        self.width = width
        self.height = width

    """
    Args Update
    """
    def update(self, *args, **kwargs):
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
