# Write a function to merge two sorted lists into a single sorted list

def merge_sorted_list(lst1, lst2):

    return sorted(lst1 + lst2)

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
print(merge_sorted_list(lst1, lst2))
