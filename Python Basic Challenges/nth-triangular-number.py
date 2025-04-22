# Write a function to calculate the nth triangular number.

def triangular_number(n):

    result = 0

    for i in range(n + 1):
        result += i

    return result

print(triangular_number(5))