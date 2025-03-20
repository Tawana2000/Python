# Write a function to convert a matrix into a dictionary 

def matrix_to_dict(matrix):

    result = {}

    for row_idx, row in enumerate(matrix):
        result[row_idx] = row

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix_to_dict(matrix))