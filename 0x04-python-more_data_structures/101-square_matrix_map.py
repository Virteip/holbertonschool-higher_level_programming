#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda lamb: list(map(lambda da: da ** 2, lamb)), matrix))
