# Write a function to calculate the lenght of the diagonal of a cube

import math
def cube_diagonal(side):

    return round(math.sqrt(3) * side, 2)

print(cube_diagonal(5))