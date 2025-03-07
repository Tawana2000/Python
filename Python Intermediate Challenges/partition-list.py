# Write a function to partition a list into two halves
# The left half should contain all elements less than the pivot and the right half should contain all elements greater than or equal to the pivot

def moving_partition(lst):

    if not list:
        return []
    
    pivot = lst[-1]

    left = [x for x in lst if x < pivot]
    right = [pivot] + [x for x in lst[:-1] if x > pivot]

    return left + right

lst = [5, 3, 8, 4, 2, 7]
print(moving_partition(lst))