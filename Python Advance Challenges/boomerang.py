# Write a function to determine if three given points can form a boomerang.
# A boomerang is defined as a set of three points that are all distinct and not in a straight line.

def is_boomerang(p1, p2, p3):

    return (p2[0] - p1[0]) * (p3[1] - p1[1]) != (p2[1] - p1[1]) * (p3[0] - p1[0])

print(is_boomerang((0, 0), (1, 1), (2, 2)))
print(is_boomerang((0, 0), (1, 2), (2, 1)))
print(is_boomerang((0, 0), (1, 2), (2, 1)))
