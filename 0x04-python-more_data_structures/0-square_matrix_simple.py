#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None

    new_matrix = []
    for row in matrix:
        new_row = []
        for e in row:
            new_row.append(e ** 2)
        new_matrix.append(new_row)

    return new_matrix
