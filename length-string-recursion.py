#Program to find the length of a string using recursion without using len()

def lenght(string):

    if string == "":
        return 0
    
    else:
        return 1 + lenght(string[1:])

string = 'spider'
print(lenght(string))