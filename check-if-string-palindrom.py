# Python program to check whether or not a string is a palindrome.
#A palindrome string is a string that reads the same backward like: hannah, level, radar 

def palindrome(s1):

    s2 = s1[::-1]  #reversing the string 

    if s2 == s1:
        print('string is palindrome')
    else:
        print('string is not palindrome')

s1 = input('Enter the string to check: ')
palindrome(s1)