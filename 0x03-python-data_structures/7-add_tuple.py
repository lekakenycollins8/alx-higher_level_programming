#!/usr/in/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Step 1: Initialize variables for the first and second elements
    element_1_a = tuple_a[0] if len(tuple_a) >= 1 else 0
    element_2_a = tuple_a[1] if len(tuple_a) >= 2 else 0

    element_1_b = tuple_b[0] if len(tuple_b) >= 1 else 0
    element_2_b = tuple_b[1] if len(tuple_b) >= 2 else 0
    # Step 2: Sum the corresponding elements
    result_first = element_1_a + element_1_b
    result_second = element_2_a + element_2_b
    # Step 3: Return the result as a tuple
    return (result_first, result_second)
