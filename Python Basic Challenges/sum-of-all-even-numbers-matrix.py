# Write a function to calculate the sum of all even numbers in a matrix.

def sum_of_evens(matrix):

    result = 0

    for row in matrix:
        for nums in row:
            if nums % 2 == 0:
                result += nums
    return result

print(sum_of_evens([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))