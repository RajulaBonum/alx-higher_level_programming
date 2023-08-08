#!/usr/bin/python3
for i in range(10):
    for j in range(1,10):
        if j == i:
            pass
        else:
            print(f"{i}{j}", end=", ")
