#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square = []
    for i in range(0, len(matrix)):
        square.append([n*n for n in matrix[i]])
    return square
