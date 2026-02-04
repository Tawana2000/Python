# Write a function to find all factors of a given number. 

def get_factors(n):

    facotrs = []

    for i in range(1, n + 1):
        if n % i == 0:
            facotrs.append(i)
    return facotrs

print(get_factors(10))
