# Write a program to remove the nth character from a given string

def rmv_char(string, n):

    if n < 0 or n >= len(string):
        print('Invalid Position!')
        return string
    
    new_string = string[:n] + string[n + 1]
    return new_string

string = input('Enter the position: ')
n = int(input('Enter the position of the character to remove: '))
result = rmv_char(string, n)
print('String after removing the characer: ', result)