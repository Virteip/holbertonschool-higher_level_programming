#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    a = " "
    for i in matrix:
        for j in i:
            print("{}".format(j), end='')
            if j != i[-1]:
                print("{}".format(a), end='')
        print()
