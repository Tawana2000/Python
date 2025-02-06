# Write a function to convert the keys and values in a dictionary to separate lists

def dict_to_lists(dict):

    keys = list(dict.keys())
    values = list(dict.values())

    return keys, values

dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(dict_to_lists(dict))