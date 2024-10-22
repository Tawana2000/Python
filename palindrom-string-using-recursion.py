# Program to check if the string is palidrom using recursion

def check_palindrom(string):

    string = string.lower()  
    if string == '' or len(string) == 1:   #return true if string is empty or has one character
        return True
    
    if string[0] == string[-1]:    #check if the first and last characters are the same
        return check_palindrom(string[1: -1])
    
    else:
        return False
string = 'Level'
print(check_palindrom(string))
