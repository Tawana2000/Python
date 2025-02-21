# Write a function to perform an iterated square root operation on a number

import math
def iterated_square_root(n):

    while n >= 2:
        n = math.sqrt(n)

    return round(n, 2)

print(iterated_square_root(256))
print(iterated_square_root(400))