#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix:
        for i in matrix:
            separate = " "
            for j in i:
                print("{}".format(j), end='')
                if j != i[-1]:
                    print("{}".format(separate), end='')
            print()
