# Write a function to check if a number is powerful or not

def is_powerful_number(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    def prime_factors(num):
        factors = {}
        factor = 2
        while factor * factor <= num:
            while num % factor == 0:
                factors[factor] = factors.get(factor, 0) + 1
                num //= factor
            factor += 1
        if num > 1:
            factors[num] = 1
        return factors

    factors = prime_factors(n)
    return all(power >= 2 for power in factors.values())


print(is_powerful_number(36))
print(is_powerful_number(18))