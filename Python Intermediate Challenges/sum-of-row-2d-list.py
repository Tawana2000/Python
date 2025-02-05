# Write a function to calculate the sum of each row in a 2D list

def row_sum(matrix):

    return [sum(row) for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(row_sum(matrix))