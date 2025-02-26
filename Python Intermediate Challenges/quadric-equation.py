# Write a function to solve a quadric equation

import math
def solve_quadric(a, b, c):

    x1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / 2 * a
    x2 = ((-b - math.sqrt((b ** 2) - 4 * a * c)) / 2 * a)

    return [x1, x2]

print(solve_quadric(1, -3, 2))