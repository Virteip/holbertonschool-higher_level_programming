#!/usr/bin/python3


def add_integer(a, b=98):
    try:
        if type(a) or type(b) is float:
            return int(a) + int(b)
    except:
        if type(a) != float and type(a) != int:
            raise TypeError("a must be an integer")
        if type(b) != float and type(b) != int:
            raise TypeError("b must be an integer")
