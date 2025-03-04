# Write a function to determine if the sum of ASCII values of all characters in a string is even or odd

def sum_of_letters(string):

    result = 0
    for char in string:

        result += ord(char)

    return 'Even' if result % 2 == 0 else 'Odd'

print(sum_of_letters('abc'))
print(sum_of_letters('abcde'))