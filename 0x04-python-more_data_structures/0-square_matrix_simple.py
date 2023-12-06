#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = list(map(lambda res: list(map(lambda x: x ** 2, res)), matrix))
    return new_m
