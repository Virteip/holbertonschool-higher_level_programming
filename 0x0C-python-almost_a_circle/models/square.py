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
