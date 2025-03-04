# Write a function to map each letter in a string to its corresponding ASCII value

def map_letter(string):

    return {char: ord(char) for char in string}

print(map_letter('abc'))