# Write a function to check if a given string is a palindrome

def is_palindrome(s):

    return True if s == s[::-1] else False

s = input('Enter the string to check: ')
print(is_palindrome(s))