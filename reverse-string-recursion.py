#Create a program to reverse a string using recursion

def reverse(string):

    if string == "":  #define base condition
        return ""
    
    return reverse(string[1:]) + string[0]   #recursive call

string = 'Vibe'
print(reverse(string))