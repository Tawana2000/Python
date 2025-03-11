# Write a function to create a dictionary with characters as keys and their ASCII codes as values

def ascii_dictionary(string):

    return {char: ord(char) for char in string}

print(ascii_dictionary('Hello'))