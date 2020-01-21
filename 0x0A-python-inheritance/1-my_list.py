#!/usr/bin/python3
"""
Create Class MyList
"""


class MyList(list):
    """
    Define method to order list by copying it
    """
    def print_sorted(self):
        copy = self.copy()
        copy = copy.sort()
        print(copy)
