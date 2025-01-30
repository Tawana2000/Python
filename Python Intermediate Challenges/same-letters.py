# Write a function to check if two strings have same letters

def equivalent_strings(str1, str2):

    if len(str1) != len(str2):
        return "Missing character for one of the strings!"
    
    if len(str1) == len(str2):

        for i in str1:
            if i in str2:
                return True
            
    return False

print(equivalent_strings('abc',  'bca'))