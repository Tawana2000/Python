# Write a function to convert a matrix of characters into a single string

def matrix_to_string(matrix):

    return ''.join(''.join(row) for row in matrix)

matrix = [['H', 'e', 'l', 'l', 'o'], ['W', 'o', 'r', 'l', 'd']]

print(matrix_to_string(matrix))