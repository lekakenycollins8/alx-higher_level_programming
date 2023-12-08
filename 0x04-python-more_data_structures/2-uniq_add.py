#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = sum({element for element in my_list})
    return uniq_sum
