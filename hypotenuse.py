# Write a function to calculate the hypotenuse of a right triangle
# for the right triangle the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides, this can be written as: a^2 + b^2 = c^2

import math
def calculate(a, b):
    return math.sqrt(a**2 + b**2)

a = int(input('Enter the length of side a: '))
b = int(input('Enter the length of side b: '))
print(calculate(a, b))