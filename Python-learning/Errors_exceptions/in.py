#!/usr/bin/python3
while True:
    try:
        number = int(input("Enter your number: "))
        print(f"{number}")
        break
    except ValueError:
        print("Error, please enter a number.")
