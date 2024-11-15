# Write a function to find the smallest number in each list from a group of lists

def find_smallest(lists):

    result = [min(sublist) for sublist in lists]
    return result

lists = [
    [5, 7, 90],
    [34, 16, 78],
    [12, 8, 45]
]

print(find_smallest(lists))