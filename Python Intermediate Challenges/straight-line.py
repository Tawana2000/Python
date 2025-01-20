# Write a function to check if given coordinates form a straight line

def is_striaght_line(coordinates):
    
    if len(coordinates) < 2:
        return False
    
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    initial_slope = float('inf') if x2 - x1 == 0 else (y2 - y1) / (x2 - x1)

    for i in range(1, len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]

        current_slope = float('inf') if x2 - x1 == 0 else (y2 - y1) / (x2 - x1)

        if current_slope != initial_slope:
            return False
        
    
    return True

coordinates = [[1,2], [2,3], [3,4], [4,5], [5,6]]
print(is_striaght_line(coordinates))