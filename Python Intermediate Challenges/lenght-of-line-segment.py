# Write a function to calculate the lenght of line segment joining two given points

import math
def calculate_line_length(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    lenght = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return f"{lenght:.2f}"

point1 = map(float, input("Enter the first point values separated by space: ").split())
point2 = map(float, input("Enter the second point values separated by space: ").split())

print(calculate_line_length(point1, point2))