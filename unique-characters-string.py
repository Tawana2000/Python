#Given a string, find and return the index of the first character that is not repeated.

def unique_char(string):


    for index, i in enumerate(string):

        if i.lower() not in string[index + 1 :].lower():
            return index
        

string = 'programiz.pro'
print(unique_char(string))
