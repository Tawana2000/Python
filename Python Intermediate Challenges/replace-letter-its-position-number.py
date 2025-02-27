# Write a function to replace each letter in a string with its position in the alphabet

def replace_with_position(s):

    return " ".join(str(ord(c) - 96) for c in s.lower() if c.isalpha())

print(replace_with_position('hello'))