# Write a function to write a function to find the second largest element in a list.

def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2] if len(lst) > 1 else None

print(second_largest([1, 2, 3, 4, 5]))
