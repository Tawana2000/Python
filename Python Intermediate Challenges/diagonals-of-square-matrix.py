# Write a function to get the diagonals of a square matrix

def get_diagonals(matrix):

    main_diagonal = [matrix[i][i] for i in range(len(matrix))]
    secondary_diagonal = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]

    return main_diagonal, secondary_diagonal

matrix = [
    [3, 6, 9],
    [14, 78, 3],
    [4, 13, 20]
]

print(get_diagonals(matrix))