# Write a function to check if one list is a subset of another

def is_subset(list1, list2):

    return all(i in list2 for i in list1)

list1 = [1, 5]
list2 = [1, 2, 3, 4]

print(is_subset(list1, list2))