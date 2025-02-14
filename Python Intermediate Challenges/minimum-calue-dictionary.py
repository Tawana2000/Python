# Write a function to get the key of the minimum value form a given dictionary

def get_min_key(dict1):

    return min(dict1, key = dict1.get)
    

dict1 = {'a': 1, 'b': 2, 'c': 3}
print(get_min_key(dict1))