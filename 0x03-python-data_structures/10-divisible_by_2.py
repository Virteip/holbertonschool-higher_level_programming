#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    save = []
    for i in my_list:
        if i % 2 == 0:
            i = True
            save.append(i)
        else:
            i = False
            save.append(i)

    return save
