# Write a function to calculate the trace of a given matrix

def calculate_matrix_trace(matrix):

    return sum(matrix[i][i] for i in range(len(matrix)))

matrix = [
    [2, 0, 1],
    [3, 4, 5],
    [6, 7, 8]
]

print(calculate_matrix_trace(matrix))