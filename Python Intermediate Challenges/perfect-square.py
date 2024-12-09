# Write a function to check if a number is a perfect square or not

import math

def is_perfect_square(n):

    return True if n % math.sqrt(n) == 0 else False

n = int(input('Enter the number to check if perfect square: '))

print(is_perfect_square(n))