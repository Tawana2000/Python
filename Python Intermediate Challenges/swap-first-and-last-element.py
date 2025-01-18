# Write a functin to swap the first and last elements of a list

def swap_elements(lst):

    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]

    return lst

lst = ['apple', 'banana', 'cherry']
print(swap_elements(lst))