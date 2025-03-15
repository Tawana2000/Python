# Write a function to determine if a number is equidigital

from collections import Counter

def prime_factorization(n):
    factors = Counter()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        factors[n] += 1
    return factors

def is_equidigital(n):
    factors = prime_factorization(n)
    factorization_digits = sum(len(str(base)) + (len(str(exp)) if exp > 1 else 0) for base, exp in factors.items())
    return factorization_digits == len(str(n))

print(is_equidigital(125))
print(is_equidigital(10))