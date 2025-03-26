# Write a function  to perform cicular shift
# A circular shift moves the elements of the list one place to the right, with the last element moving to the first place

def circular_shift(lst):
    
    result = []

    result.append(lst[-1])
    del lst[-1]
    lst.insert(0, result[0])

    return lst

lst = [1, 2, 3, 4, 5]
print(circular_shift(lst))