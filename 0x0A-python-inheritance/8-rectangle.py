#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    Raise an exception for area not defined
    """
    def area(self):
        raise Exception("area() is not implemented")

    """
    Validate Value type and #
    """
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
"""
Class Rectangle
"""


class Rectangle(BaseGeometry):
    """
    Constructor method initializer
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
