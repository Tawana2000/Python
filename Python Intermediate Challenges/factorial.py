# Write a function to calculate the factorial of a number

def calculate_factorial(n):

    factorial = 1

    if n == 0 and n == 1:
        return 1
    
    for i in range(1, n + 1):
        factorial *= i

    return factorial

n = 5
print(calculate_factorial(n))