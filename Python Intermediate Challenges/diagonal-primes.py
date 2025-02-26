# Write a function to find out if the diagonal elements of a square matrix are prime numbers

def is_prime_diagonal(matrix):

    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("Input must be a non-empty square matrix")
    
    n = len(matrix)
    
    for i in range(n):
        num = matrix[i][i]
        if num < 2:
            return False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                return False
    
    return True

matrix1 = [
    [2, 1, 4],
    [3, 3, 6],
    [5, 8, 7]
] 

matrix2 = [
    [2, 1],
    [3, 4]
]

matrix3 = [
    [3, 1, 4],
    [2, 5, 6],
    [8, 9, 7]
]

print(is_prime_diagonal(matrix1))
print(is_prime_diagonal(matrix2)) 
print(is_prime_diagonal(matrix3))
