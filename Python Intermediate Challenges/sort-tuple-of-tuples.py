# Write a function to sort a tuple of tuples by the second item in each tuple

def sort_tuples(tuples):

    return tuple[sorted(tuples, key = lambda x: x[1])]

print(sort_tuples(((1, 3), (4, 2), (2, 5))))
print(sort_tuples(((10, 15), (7, 8), (5, 12))))