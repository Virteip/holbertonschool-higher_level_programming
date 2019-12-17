#!/usr/bin/python3


def element_at(my_list, idx):
    i = 0

    for i in my_list:
        i = i+1

    if idx < 0 or idx > i:
        return None

    if idx in my_list:
        return my_list[idx]
