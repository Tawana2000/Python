# Write a function to solve an exponential equation using logarithms.

import math
def solve_exponential(base, result):

    if base <= 0 or result <= 0:
        return 'Not Valid Input'
    return round(math.log(result, base))

print(solve_exponential(2, 8))       