# Write a function to add the values of symbols in a matrix

def add_matrix_values(matrix):

    total, operator = 0, '+'
    for row in matrix:
        for val in row:
            if isinstance(val, int):
                total = eval(f"{total} {operator} {val}")

            elif val in '+-*/':
                operator = val

    return total

matrix = [[1, '+', 2], ['-', 3], ['*', 2]]
print(add_matrix_values(matrix))