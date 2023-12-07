#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = [] #new row for result matrix
        for element in row:
            sq_element = element ** 2
            new_row.append(sq_element) #append sq_element to new_row
        new_matrix.append(new_row) #append new row to result matrix
    return new_matrix
