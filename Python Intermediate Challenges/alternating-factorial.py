# Write a function to calculate the alternating factorial of a number
# odd factorials are subtracted and even factorials are added

def alternating_factorials(n):
    
    fact = 1

    if n == 0 or n == 1:
        return 1
    
    for i in range(1, n + 1):
        fact *= i
    
    return fact

def factorials(n):

    total = 0

    for j in range(1, n + 1):

        if j % 2 == 0:
            total += alternating_factorials(j)

        else:
            total -= alternating_factorials(j)

    return total

n = 4

print(factorials(n))