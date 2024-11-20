# Write a function to check if one list is a subset of another

def is_subset(list1, list2):

    for items in list1:
        if items not in list2:
            return False
    
    return True

list1 = [1,2,3]
list2 = [1,2]

print(is_subset(list1, list2))