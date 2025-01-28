# Write a function to calculate the volume of a cone

import math
def valume_of_cone(height, radius):

    volume = (1/3) * math.pi * (radius ** 2) * height
    return f"{volume:0.2f}"

height = int(input("Enter the Cone's height: "))
radius = int(input("Enter the Cone's radius: "))
print(valume_of_cone(height, radius))