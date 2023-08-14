#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix[j])):
            print("{}".format((matrix[j][i])),sep=" ", end="")
            if i < len(matrix[j]) - 1:
                print(" ", end="")
        print()
