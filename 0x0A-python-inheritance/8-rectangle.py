#!/usr/bin/python3
"""
Class BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

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
