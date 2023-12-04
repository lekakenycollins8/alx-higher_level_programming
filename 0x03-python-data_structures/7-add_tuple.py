#!/usr/in/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    element_1_a = tuple_a[0] if len1 > 0 else 0
    element_2_a = tuple_a[1] if len1 > 1 else 0

    element_1_b = tuple_b[0] if len2 > 0 else 0
    element_2_b = tuple_b[1] if len2 > 1 else 0
    return ("{:d}".format((element_1_a + element_1_b, element_2_a + element_2_b)))
