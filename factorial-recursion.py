#Create a program to find the factorial of a number using recursion.

def factorial(n):

    if n == 0:
        return 1
    
    return n * factorial(n - 1)
    
n = 4
print(factorial(n))