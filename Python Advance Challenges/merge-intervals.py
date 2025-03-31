# Write a function to merge all overlapping intervals.

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
print(merge(intervals))
