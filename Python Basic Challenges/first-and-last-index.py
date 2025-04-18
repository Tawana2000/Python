# Write a function to find the first and last index of a given element in a list

def first_last_index(lst, n):

    if n not in lst:
        return (-1, -1)
    first = lst.index(n)
    last = len(lst) - 1 - lst[::-1].index(n)
    return (first, last)
    
print(first_last_index([1, 2, 3, 2, 4, 2], 2))