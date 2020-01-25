#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        super().__init__(width)
        super().__init__(height)
        super().__init__(x)
        super().__init__(y)

    """
    Print string with str
    """
    def __str__(self):
        return "[Square] " + "(" + str(self.id) + ") " + str(self.__x) + "/" + str(self.__y)
