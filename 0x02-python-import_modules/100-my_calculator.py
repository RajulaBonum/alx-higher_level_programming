#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

args = sys.argv[1:]
i = len(args)
if i == 3:
    a = args[0]
    op = args[1]
    b = args[2]
    if op == '+':
        print("{} + {} = {}".format((a), (b), (int(add(a, b)))))
    elif op == '-':
        print("{} - {} = {}".format((a), (b), (int(sub(a, b)))))
    elif op == '*':
        print("{} * {} = {}".format((a), (b), (int(mul(a, b)))))
    elif op == '/':
        print("{} / {} = {}".format((a), (b), (int(div(a, b)))))
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
else:
    print("Usage: .100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
