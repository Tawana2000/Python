# Write a function to calculate the lenght of line segment joining two given points

import math
def calculate_line_lenght(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    lenght = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(lenght, 2)

print(calculate_line_lenght((15, 7), (22, 11)))