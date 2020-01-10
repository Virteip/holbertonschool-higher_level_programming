#!/usr/bin/python3
"""
Class to define a Square with private size variable
"""


class Square:
    """
    Init method to set size variable and exceptions to be raised in case
    conditions are not met.
    """
    def __init__(self, size=0):
        if type(size) == int and size >= 0:
            self.__size = size
        elif type(size) != int:
            raise NameError("size must be an integer")
        elif size < 0:
            raise NameError("size must be >= 0")

    """
    Area function to calculate are size of square.
    """
    def area(self):
        return pow(self.__size, 2)

    """
    Setter function.
    """
    def size(self, value):
        if type(size) == int and size >= 0:
            self.__size = value
        elif type(size) != int:
            raise NameError("size must be an integer")
        elif size < 0:
            raise NameError("size must be >= 0")

    """
    Getter function.
    """
    def size(self):
        return self.__size
