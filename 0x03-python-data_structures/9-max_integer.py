#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None
    max_v = 0

    for i in my_list:
        if my_list[+1] > max_v:
            max_v = i

    return max_v
