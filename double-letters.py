# Write a function to double every letter in a given string

def double_letter(string):

    result = ''

    for char in string:
        result += char * 2

    return result

print(double_letter('hello'))