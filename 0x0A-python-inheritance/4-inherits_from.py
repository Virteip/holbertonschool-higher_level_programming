#!/usr/bin/python3
"""
Check if instance is inherited
"""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class
