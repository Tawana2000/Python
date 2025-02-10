# Write a function to determine if a number is equidigital

def count_digits(num):
    return len(str(num))

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def is_equidigital(n):
    if n < 2:
        return False

    factor_digits = sum(count_digits(factor) for factor in prime_factors(n))
    number_digits = count_digits(n)
    
    return factor_digits == number_digits

print(is_equidigital(10)) 
print(is_equidigital(12))