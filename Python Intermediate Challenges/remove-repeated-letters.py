# Write a function to remove the repeated letters from a given string

def remove_repeated_letters(s):

    new_str = ''

    for char in s:
        if char not in new_str:
            new_str += char

    return new_str

print(remove_repeated_letters('hello world'))