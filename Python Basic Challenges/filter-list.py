# Write a function to filter out only the integers from a list

def filter_integers(lst):
    
    return [num for num in lst if type(num) == int]

print(filter_integers([1, 'a', 2, 'b', 3]))