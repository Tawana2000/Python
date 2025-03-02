# Write a function to concatenate two lists to match a target list

def concatenate_lists(list1, list2, target):

    result = list1 + list2

    return True if target == result else False

list1 = ['a', 'b']
list2 = ['c', 'd']
target = ['a', 'b', 'c', 'd']

print(concatenate_lists(list1, list2, target))