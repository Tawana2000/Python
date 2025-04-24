# Write a function to return the interval between two faces on a clock.
# The shortest distance between two clock faces can be either clockwise or counterclockwise

def calculate_clock_interval(face1, face2):

    return min((face2 - face1) % 12, (face1 - face2) % 12)

print(calculate_clock_interval(10, 6))
print(calculate_clock_interval(3, 9))