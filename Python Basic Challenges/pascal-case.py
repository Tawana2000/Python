# Write a function to convert a given string to Pascal Case.

def to_pascal_case(s):

    words = s.replace('_', ' ').split()
    return ''.join(word.capitalize() for word in words)

print(to_pascal_case('Hello World'))