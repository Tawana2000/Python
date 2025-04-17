# Write a function to create a new set that contains the identical items from two give sets.

def identical_items(set1, set2):

    return set1.intersection(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(identical_items(set1, set2))