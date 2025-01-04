# Write a function to calculate the difference between two colors using the Euclidean distance formula
# The Euclidean distance between two points in three dimentional space is given by: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2), each dimension corresponds to one of the RGB values of a color
import math
def color_difference(color1, color2):

    if len(color1) != 3 or len(color2) != 3:
        raise ValueError("Each color must be a tuple of 3 values, representing the RGB color!")
    
    return math.sqrt(sum((c2 - c1) ** 2 for c1, c2 in zip(color1, color2)))

color1 = (255, 255, 255)
color2 = (0, 0, 0)
print(f"{color_difference(color1, color2): .2f}")