# Write a function to complete a square matrix by filling in missing elements with zeroes

def complete_square_matrix(matrix):
    max_size = max(len(matrix), max(len(row) for row in matrix))
    return [row + [0] * (max_size - len(row)) for row in matrix] + [[0] * max_size] * (max_size - len(matrix))

input_matrix = [
    [1, 2],
    [3, 4],
    [5, 6, 7]
]

result = complete_square_matrix(input_matrix)
for row in result:
    print(row)
