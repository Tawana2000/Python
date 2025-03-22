# Write a function to merge overlapping intervals

def merge_intervals(intervals):

    intervals.sort()
    result = []

    for i in intervals:
        if result and i[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], i[1])

        else:
            result.append(i)

    return result

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))