# Write a function to calculate the difference between consecutive elements in a list until the list has only one element left

def n_differences(lst):
    
    while len(lst) > 1:
        lst = [abs(b - a) for a, b in zip(lst, lst[1:])]

    return lst[0]
    
print(n_differences([5, 2, 1]))
print(n_differences([3, 7, 11]))