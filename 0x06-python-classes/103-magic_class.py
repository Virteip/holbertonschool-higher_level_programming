#!/usr/bin/python3
import math
"""
Magic Class
"""


class MagicClass:

    def circumference(self):
        return (2 * math.pi * self.__radius)

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return ((self.__radius ** 2) * math.pi)
