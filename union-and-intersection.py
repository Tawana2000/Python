# Write a function to find the union and intersection of two lists in sorted order.

def find_union_intersec(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    intersection = set1.intersection(set2)

    union = set1.union(set2)

    return sorted(list(union)), list(intersection)
    
list1 = [1,2,3,4]
list2 = [3,4,5,6]
print(find_union_intersec(list1, list2))