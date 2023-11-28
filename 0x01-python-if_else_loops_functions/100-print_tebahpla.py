#!/usr/bin/python3

for alphabet in range(122, 96, -1):
    print("{}".format(chr(alphabet).lower()
        if alphabet % 2 == 0 else chr(alphabet).upper()), end="")
