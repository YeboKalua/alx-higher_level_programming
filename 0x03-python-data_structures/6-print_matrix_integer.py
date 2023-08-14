#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = " ".join(str(element) for element in row)
        print(formatted_row)
