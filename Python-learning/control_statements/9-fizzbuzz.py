#!/usr/bin/python3
for i in range (0, 100):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz", end=" ")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz", end=" ")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    else:
        print(f"{i}", end=" ")
print()
