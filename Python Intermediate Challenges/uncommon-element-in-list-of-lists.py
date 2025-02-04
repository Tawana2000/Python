# Write a function to find and return the uncommon elements in a list of lists

def uncommon_elements(lists):

    elements = [item for sublist in lists for item in sublist]
    return [x for x in elements if elements.count(x) == 1]

lists = [[1, 2, 3], [2, 3, 4,], [4, 5, 6]]
print(uncommon_elements(lists))
