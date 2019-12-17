#!/usr/bin/python3


def no_c(my_string):
    new = ""
    chars = "Cc"
    counter = 0

    for iterate in my_string:
        if iterate not in chars:
            new = new + my_string[counter]
        counter = counter + 1

    return new
