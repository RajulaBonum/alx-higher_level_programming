#!/usr/bin/python3
def no_c(my_string):
    new = my_string
    for i in new:
        if new[int(i)] == 99 or new[int(i)] == 67:
            new[i] = ""
        else:
            pass
    return new
