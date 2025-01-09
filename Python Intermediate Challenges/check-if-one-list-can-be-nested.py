# Write a function to check if one list can be nested in another

def can_be_nested(list1, list2):

    list1 = sorted(list1)
    list2 = sorted(list2)

    if list1[0] > list2[0] and list1[-1] < list2[-1]:
        return True
    else:
        return False
    
list1 = [1, 2, 3, 4]
list2 = [0, 6]

print(can_be_nested(list1, list2))