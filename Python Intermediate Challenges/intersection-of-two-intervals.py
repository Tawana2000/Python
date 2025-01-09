# Write a function to find the intersection of two intervals

def intersection(interval1, interval2):
    
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start <= end:
        return [start, end]  # Valid intersection
    return []  # No intersection


interval1 = [1, 5]
interval2 = [3, 7]
print(intersection(interval1, interval2))  

# Case with no intersection
interval1 = [1, 2]
interval2 = [3, 4]
print(intersection(interval1, interval2))
