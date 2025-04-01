# Write a funtion to find the m-th smallest value in k sorted lists

def mth_smallest(lists, m):
    return sorted(sum(lists, []))[m - 1]


print(mth_smallest([[1, 3, 5], [2, 4, 6], [0, 7, 8], [9, 10, 11]], 5)) 