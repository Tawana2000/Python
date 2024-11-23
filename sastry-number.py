# Write a function to check if a number is a Sastary number

import math

def is_sastary(n):

    result = str(n) + str(n + 1)

    if n < 0:
        return False
    
    sqrt_n = math.sqrt(int(result))
    return sqrt_n == int(sqrt_n)
    
n = 182

print(is_sastary(n))
