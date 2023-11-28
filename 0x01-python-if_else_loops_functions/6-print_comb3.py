#!/usr/bin/python3
for number in range(9):
    for digit in range(number + 1, 10):
        if number < 8:
            print("{}{}".format(number % 10, digit % 10), end=", ")
        else:
            print("{}{}".format(number % 10, digit % 10), end="\n")
