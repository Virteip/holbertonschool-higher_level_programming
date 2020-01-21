#!/usr/bin/python3
"""
Class Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Constructor method initializer
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
    """
    Calculate and return square area
    """
    def area(self):
        return self.__size * self.__size
