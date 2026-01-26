#John's primary language is Arabic, and his English is not so good. He has yet to learn about punctuations and letter casings. Now, write a Python program that cleans the string in such a way that it becomes readable. To do this,
# Remove extra spaces from both ends. Capitalize only the first character. Add a dot at the end.

def improve_english(string):

    string = string.strip()  #removes spaces
    string = string.capitalize()
    string = string + '.'

    return string

string = input('Type your words: ')
print(improve_english(string))

