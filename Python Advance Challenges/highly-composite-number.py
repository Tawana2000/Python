# Write a function to check if a number is highly composite number.
# A highly composite number is a positive integer with more divisors than any smaller positive integer

def is_highly_composite(n):
    n_divisors = sum(1 for i in range(1, n + 1) if n % i == 0)
    
    for i in range(1, n):
        i_divisors = sum(1 for j in range(1, i + 1) if i % j == 0)
        if i_divisors >= n_divisors:
            return False
    return True

# Test case
print(is_highly_composite(12))  # Output: True
print(is_highly_composite(9))
print(is_highly_composite(23))
print(is_highly_composite(56))
