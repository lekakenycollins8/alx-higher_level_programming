#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    el_1_a = tuple_a[0] if len1 > 0 else 0
    el_2_a = tuple_a[1] if len1 > 1 else 0

    el_1_b = tuple_b[0] if len2 > 0 else 0
    el_2_b = tuple_b[1] if len2 > 1 else 0
    return ("{}".format((el_1_a + el_1_b, el_2_a + el_2_b)))
