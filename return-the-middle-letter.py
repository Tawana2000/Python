#Create a function that will return the middle letter of the passed string. If there is no middle letter, return an empty string.

def mid(string):


    if len(string) % 2 == 0:
        return ''
        
    middle = len(string) // 2
    letter = string[middle]
    return letter

letter = mid('country')   
print(letter)