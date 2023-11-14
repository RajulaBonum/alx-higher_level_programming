#!/usr/bin/python3
binary = [] 
for i in range(0, 10):
    quotient = i / 2
    if quotient != 0:
        modulus = int (quotient % 2)
        binary.append(modulus)
    print(f"{i} = {binary}")
