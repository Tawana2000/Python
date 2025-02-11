# Write a function to check if a given string can become a palindrome by removing at most one character

def valid_palindrome(s):

    def is_palindrome(string):
        return string == string[::-1]
    
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s[left:right]) or is_palindrome(s[left + 1:right + 1])
        
        left += 1
        right -= 1

    return True

print(valid_palindrome('abca'))
print(valid_palindrome('abcdef'))