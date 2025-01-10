# Write a function to calculate the area of circumcircle and incircle when the area of a square is given 

import math
def circle_areas(square_area):
    side = math.sqrt(square_area)
    
    # Circumcircle
    circum_radius = (side * math.sqrt(2)) / 2
    circum_area = math.pi * circum_radius**2
    
    # Incircle
    in_radius = side / 2
    in_area = math.pi * in_radius**2
    
    return {"circumcircle_area": circum_area, "incircle_area": in_area}

square_area = 16
result = circle_areas(square_area)
print(f"Circumcircle Area: {result['circumcircle_area']:.2f}")
print(f"Incircle Area: {result['incircle_area']:.2f}")
