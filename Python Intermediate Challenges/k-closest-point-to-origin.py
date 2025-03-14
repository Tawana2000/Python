# Write a function that finds the closest point to the origin (0, 0) from a given list of points

import math
def closest_points(points_list, k):

    return sorted(points_list, key = lambda p: p[0]**2 + p[1]**2)[:k]

points = [(3,-4),(5,-6),(7,-8)]
print(closest_points(points, 3))