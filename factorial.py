#write a function to write the factorial of a number

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = 5
print(factorial(n))