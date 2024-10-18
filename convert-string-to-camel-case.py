#Write a function to convert a given string to camel case

def came_case(string):

    words = string.split()

    camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    return camel_case

string = 'hello world'
print(came_case(string))