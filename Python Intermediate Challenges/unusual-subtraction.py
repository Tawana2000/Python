# Write a function to perform an unusual subtraction operation on two strings
# Remove the last character from the first string for each character in the second string

def unusal_subtraction(str1, str2):

    for _ in str2:
        if str1:
            str1 = str1[:-1]
        else:
            break

    return str1

str1  = 'abcdef'
str2 = '123'

print(unusal_subtraction(str1, str2))