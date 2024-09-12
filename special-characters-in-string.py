#Create a Python program to find the total number of special characters in a string.

def character_counter(string):

    counter = 0
    

    for i in string:
        if not i.isalpha() and not i.isdigit() and not i.isspace():
            counter += 1

    return counter

        
string = 'hello! good morning *.'
print(character_counter(string))
