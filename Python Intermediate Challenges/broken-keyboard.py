# Write a function to check if a given string can be typed using a broken keyboard

def can_type(keys, word):

    for char in word:
        if char not in keys:
            return False
        
    return True


keys = input('Enter the key characters: ')
word = input('Enter the word to check if present in the working keys: ')
print(can_type(keys, word))
