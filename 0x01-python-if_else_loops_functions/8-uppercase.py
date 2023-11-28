#!/usr/bin/python3

def uppercase(str):
    upcase_str = ""

    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upcase_str += chr(ord(char) - 32)
        else:
            upcase_str += char
    print("{}".format(upcase_str), end="\n")
