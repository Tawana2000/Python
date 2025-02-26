# Write a function to calculate the shortest distance between two points in a 2D plane.

import math
def calculate_distance(point1, point2):

    return round(math.dist(point1, point2), 2)

print(calculate_distance((1, 1), (4, 5)))