# Write a function to generate a list of prime factors for a given number

def prime_factors(n):

    factors = []  
    divisor = 2

    while n > 1:
        while n % divisor == 0:  # Check if divisor is a factor
            factors.append(divisor)
            while n % divisor == 0:
                n //= divisor  # Reduce n by dividing it by the factor
        divisor += 1  # Move to the next potential factor
        if divisor * divisor > n:  # If divisor exceeds √n, n itself is a prime factor
            if n > 1:
                factors.append(n)
                break

    return factors

print(prime_factors(60))