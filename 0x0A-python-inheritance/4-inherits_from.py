#!/usr/bin/python3
"""
Check if instance is inherited
"""


def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    else:
        return True
