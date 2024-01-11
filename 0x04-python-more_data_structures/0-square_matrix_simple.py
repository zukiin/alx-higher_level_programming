#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return list(list(map(lambda x: x*x, new_list)) for new_list in matrix)
