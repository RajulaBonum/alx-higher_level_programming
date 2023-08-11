#!/usr/bin/python3
import sys
args = (sys.argv[1:])
result = 0
i = len(args)
if i >= 1:
    for i in range(len(args)):
        result += int(args[i])
    print("{}".format(result))
else:
    print(0)
