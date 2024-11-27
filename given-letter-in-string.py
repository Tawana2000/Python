# Write a function to check if a given letter is present in a given string

def if_present(string, letter):

    for i in string:
        if i == letter:
            return True
        
    return False

string = input('Enter the string: ')
letter = input('Enter the letter to check: ')

print(if_present(string, letter))