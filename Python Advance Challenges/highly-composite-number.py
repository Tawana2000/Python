# Write a function to check if a number is a highly composite number.
# A higly composite number is a positive integer with more divisors than any smaller positive integer has

def is_highly_composite(n):
  n_divisors = sum(1 for i in range(1, n+1) if n % i == 0)
  for i in range(1, n):
    if i_divisors >= n_disisors:
      return False
