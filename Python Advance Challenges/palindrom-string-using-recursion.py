# Write a function to check if a given phrase is palindrome using recursion

def is_palindrome(s):

    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


print(is_palindrome('racecar')) 
print(is_palindrome('python'))