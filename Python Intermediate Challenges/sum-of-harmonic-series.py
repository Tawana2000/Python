# Write a function to calculate the sum of the harmonic series up to a given number

def harmonic_sum(n):

    result = 0

    for i in range(1, n + 1):

        result += 1 / i

    return round(result, 2)

print(harmonic_sum(5))