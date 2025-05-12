# Write a function to find the median of a list of integers 

def find_median(lst):

    lst.sort() 

    median = len(lst) // 2
    return (lst[median] + lst[median - 1]) / 2 if len(lst) % 2 == 0 else lst[median]

print(find_median([1, 3, 2]))
print(find_median([1, 6, 4, 2]))
