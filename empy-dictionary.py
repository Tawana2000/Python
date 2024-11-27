# Write a function to check if a given dictionary is empty or not

def is_empty(dictionary):

    if not dictionary:
        return True
    
    else:
        return False
    

dictionary = {}
print(is_empty(dictionary))

dictionary = {'a': 1}

print(is_empty(dictionary))