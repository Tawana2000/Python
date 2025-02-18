# Write a function to find the pair of elements in a list with the minimum difference

def min_difference_pair(lst):

    lst.sort()
    return min(((lst[i], lst[i + 1]) for i in range(len(lst) - 1)), key = lambda x: x[1] - x[0])

print(min_difference_pair([4, 2, 9, 7, 1]))