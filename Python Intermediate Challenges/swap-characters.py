# Write a function to swap two characters in a string

def double_character_swap(text, char1, char2):

    return text.replace(char1, "#").replace(char2, char1).replace("#", char2)

print(double_character_swap('hello world', 'h', 'w'))