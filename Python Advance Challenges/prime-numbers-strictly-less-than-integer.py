# Write a function to return the number of prime numbers that are stricly less than a given integer

def count_primes_less_than_n(n):
    count = 0
    for i in range(2, n):
        is_prime = True
        for divisor in range(2, int(i ** 0.5) + 1):
            if i % divisor == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

print(count_primes_less_than_n(20))