#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix =[]

    for row in matrix:
    
        squared_row = list(map(lambda x: x**2, row))
        
        result_matrix.append(squared_row)
    
    return result_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

