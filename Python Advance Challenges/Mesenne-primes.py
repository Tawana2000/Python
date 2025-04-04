# Write a function to find the all Mersenne primes up to a given number
# A Mersenne number is a number in the form M_p = 2 ^ p - 1

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def lucas_lehmer(p):
    if p == 2:
        return True
    s = 4
    m = (2 ** p) - 1
    for _ in range(p - 2):
        s = (s * s - 2) % m
    return s == 0

def mersenne_primes(n):
    result = []
    for p in range(2, n + 1):
        if is_prime(p):
            if lucas_lehmer(p):
                result.append((2 ** p) - 1)
    return result

print(mersenne_primes(130))