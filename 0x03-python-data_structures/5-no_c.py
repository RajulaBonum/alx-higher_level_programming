#!/usr/bin/python3
def no_c(my_string):
    new = my_string
    for i, j in new:
        if j == 'c':
            new[i] = ""
        elif j == 'C':
            new[i] = ""
    return new
