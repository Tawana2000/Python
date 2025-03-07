# Write a function to find the vertex of a quadratic equation

def find_vertex(a, b, c):

    x_coordinate = -b/ (2 * a)
    y_coordinate = a * (x_coordinate ** 2) + (b * x_coordinate) + c

    return x_coordinate, y_coordinate

print(find_vertex(2, -4, 2))