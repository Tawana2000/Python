# Write a function to find the missing letter in a given string of consecutive aphabets

def find_missing_letter(s):

    for i in range(len(s) - 1):

        if ord(s[i + 1]) != ord(s[i]) + 1:
            return chr(ord(s[i]) + 1)
        
    return None

print(find_missing_letter('abdef'))