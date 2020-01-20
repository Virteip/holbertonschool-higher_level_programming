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
