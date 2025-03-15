# Write a function to find all Mersenne primes up to a given number

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def mersenne_primes(limit):
    mersenne_primes_list = []
    p = 1
    while True:
        mersenne_number = (2 ** p) - 1
        if mersenne_number > limit:
            break
        if is_prime(mersenne_number):
            mersenne_primes_list.append(mersenne_number)
        p += 1
    return mersenne_primes_list


print(mersenne_primes(130))
