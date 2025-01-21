# Write a function to subtract two metrix
def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")

    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    return result

matrix1 = [
    [5, 8, 3],
    [6, 2, 9],
    [4, 7, 1]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = subtract_matrices(matrix1, matrix2)
print(result)
