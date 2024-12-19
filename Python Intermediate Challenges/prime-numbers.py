# Write a function to find all prime numbers less than a given number

def prime_less_than(n):

    if n <= 2:
        return []
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False


    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

print(prime_less_than(20))