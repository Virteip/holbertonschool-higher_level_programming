#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list:
        my_new_list = my_list

    if idx < 0 or idx >= len(my_new_list):
        return my_new_list

    my_new_list[idx] = element

    return my_new_list
