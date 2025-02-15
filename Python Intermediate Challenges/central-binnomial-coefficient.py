# Write a function to calculate the central binomial coefficient for a given number

def central_binomial_coefficient(n):

    factorial_n = 1
    factorial_2n = 1

    for i in range(1, n + 1):
        factorial_n *= i

    for j in range(1, 2 * n + 1):
        factorial_2n *= j

    cbc = (factorial_2n) // (factorial_n) ** 2
    return cbc

print(central_binomial_coefficient(4))