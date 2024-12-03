# Write a function to check if the first and last characters of a string are equal

def check_char(s):
    return True if list(s[0]) == list(s[-1]) else False


s = 'hello'
print(check_char(s))

s = 'a'
print(check_char(s))