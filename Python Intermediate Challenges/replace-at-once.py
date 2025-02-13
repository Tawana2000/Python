# Write a function to replace multiple different characters in a string at once

def replace_chars(string, replacement):

    for old, new in replacement.items():
        string = string.replace(old, new)

    return string

string = 'hello world'
replacement = {'h':'j', 'e':'i', 'l':'m'}

print(replace_chars(string, replacement))