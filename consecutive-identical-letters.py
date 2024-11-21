# Write a function to check if a string contains two consecutive identical letters

def has_consecutive_letters(s):

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
        
    return False

print(has_consecutive_letters('helo'))
