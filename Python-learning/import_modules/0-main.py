#!/usr/bin/python3
"""importing multiple functions from one file"""

if __name__ == '__main__':
    from calc_0 import sum1, sub, div, mul

"""We will use variables a and b to compute"""
a = 10
b = 7
print(sum1(a, b))
print(sub(a, b))
print(div(a, b))
print(mul(a, b))
