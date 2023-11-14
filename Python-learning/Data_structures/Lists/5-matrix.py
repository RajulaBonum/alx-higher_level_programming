#!/usr/bin/python3
"""Function that prints a matrix"""
def print_matrix(matrix=[[]]):
    for i in matrix:
        for j in i:
            print(f"{j}",end=" ")
        print("$")
