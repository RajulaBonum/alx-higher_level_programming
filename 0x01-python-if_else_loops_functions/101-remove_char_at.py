#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        return str
    str1 = ""
    for i in range(len(str)):
        if i != n:
            str1 += str[i]
    return str1
