# Write a function to generate the juggler sequence for a given number
"""
The Juggler sequence starts with a positive integer. Each subsequent term is found by taking the square root of the previous term if the previous term is even, and the square root of its cube if it's odd. All operations are rounded down to their nearest integer.
"""

import math

def juggler_sequence(n):

    if n <= 0:
        raise ValueError("Input must be a positive integer!")
    
    current_term = n
    result = [n]

    while current_term != 1:
        if current_term % 2 == 0:
            current_term = math.floor(math.sqrt(current_term))
        else:
            current_term = math.floor(current_term **  (3/2))
        result.append(current_term)

    return result

print(juggler_sequence(3))