# Write a function to check if a given square matrix is diagonally dominant
# A square matrix is said to be diagonally dominant if for every row, the sum of the diagonal element in a row is larger than or equal to the absolute sum of all the other (non-diagonal) elements in that row

def is_diagonally_dominant(matrix):

    for i in range(len(matrix)):
        diagonal = abs(matrix[i][i])
        non_diagonal_sum = sum(abs(matrix[i][j]) for j in range(len(matrix)) if j != i)

        if diagonal < non_diagonal_sum:
            return False
        
    return True

print(is_diagonally_dominant([[3, -2, 1], [1, 4, -1], [2, -1, 3]]))
print(is_diagonally_dominant([[2, 1, 1], [1, 2, 2], [1, 1, 3]]))