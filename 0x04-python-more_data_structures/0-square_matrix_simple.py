#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    i = 0
    while i < len(matrix):
        n = list(map(lambda x: (x*x), matrix[i]))
        new.append(n)
        i += 1
    return new
