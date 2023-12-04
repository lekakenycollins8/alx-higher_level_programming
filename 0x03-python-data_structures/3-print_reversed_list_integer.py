#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = my_list[-1:-(len(my_list) + 1):-1]
    for element in reverse:
        print("{:d}".format(element))
