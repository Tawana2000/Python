# Write a function to check if all the letters in a given string are neighboring letters in the alphabet

def check_neighboring_letters(s):

    for i in range(len(s) - 1):

        if ord(s[i + 1]) != ord(s[i]) + 1:
            return False
        
    return True

print(check_neighboring_letters('abcd'))
print(check_neighboring_letters('abdef'))