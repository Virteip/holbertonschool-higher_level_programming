#!/usr/bin/python3
"""
Function to divide elements of a matrix.
@div
@matrix
"""


def matrix_divided(matrix, div):
    comp = 0
    if not matrix:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    for i in matrix:
        if comp != 0 and len(i) != comp:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        comp = len(i)

    return list(map(lambda lamb:
                    list(map(lambda da: round(da / div, 2), lamb)), matrix))
