#!/usr/bin/python3
for lowercase in range(97, 123):
    if lowercase == 101 or lowercase == 113:
        continue
    print("{}".format(chr(lowercase)), end="")
