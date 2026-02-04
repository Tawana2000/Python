# Write a function to find the maximum number of points that lie on the same straight line

def max_points_on_line(points):

    if not points:
        return 0
    
    max_points = 1

    for i in range(len(points)):
        slopes = {}
        for j in range(i + 1, len(points)):
            dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
            slope = dy / dx if dx else "inf"
            slopes[slope] = slopes.get(slope, 1) + 1

        max_points = max(max_points, max(slopes.values(), default = 1))
        
    #Return the max points    
    return max_points

print(max_points_on_line([(0,0), (1, 1), (2, 2)]))
