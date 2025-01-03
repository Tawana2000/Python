# Write a function to calculate the factorial of factorials for a given number

def factorial_of_factorials(n):

    fact = 1
    fact_fact = 1
    
    if n < 0:
        return "Input must be a positive number!"
    
    for i in range(1, n + 1):
        fact = fact * i
        fact_fact *= fact

    return fact_fact
n = int(input("Enter the number to find it's factorial: "))

print(factorial_of_factorials(n))