#!/usr/bin/python3


def multiply_by_2(a_dictionary):
        dictionary = a_dictionary.copy()
        dictionary.update((key, value*2) for key, value in dictionary.items())
        return dictionary
