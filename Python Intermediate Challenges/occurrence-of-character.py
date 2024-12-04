# Write a function to find the occurrence of a character in the string

def character_occurrence(string, char):

    count = 0

    for i in string:
        if i == char:
            count += 1

    return count

string = 'Hello World'
char = input('Enter the character to check: ')
print(character_occurrence(string, char))