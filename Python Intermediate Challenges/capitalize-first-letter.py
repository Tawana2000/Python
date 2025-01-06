# Write a function to capitalize the first letter of a string based on its ASCII value
# This PR will capitalize the first letter if it's ASCII value is even

def capitalize(s):

    if s and ord(s[0]) % 2 == 0:
        s = s[0].upper() + s[1:]

    return s

s = input("Enter a string: ")
print(capitalize(s))