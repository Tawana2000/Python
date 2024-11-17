# Write a function to check if a given key exists in a dictionary 

def key_exist(dict, key):

    return key in dict

dict = {'a': 1, 'b': 2}
key = input()

print(key_exist(dict, key))