#!/usr/bin/python3
"""
MyInt Class
"""


class MyInt(int):
    """
    eq
    """
    def __eq__(self, value):
        return int(self) != int(value)
    """
    ne
    """
    def __ne__(self, other):
        return int.__eq__(self, other)
