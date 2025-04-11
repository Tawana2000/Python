# Write a function to check if a given number is Palindrome or not

def is_palindrome(n):
    n1 = str(n)
    return True if n1 == n1[::-1] else False

print(is_palindrome(121))
print(is_palindrome(43))
