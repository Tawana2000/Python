# Write a function to convert a given string into camelCase

def to_camel_case(string):

    if not string.strip():
        return ''
    
    string = string.replace('_', ' ').replace('-', ' ')

    words = string.split()

    camel_case_str = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    return camel_case_str
    
string = input('Enter the string to convert to camel case: ')

print(to_camel_case(string))