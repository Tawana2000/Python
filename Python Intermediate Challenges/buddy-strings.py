# Write a functio to determine if two strings are buddy strings

def are_buddy_strings(str1, str2):

    if len(str1) != len(str2):
        return False
    
    if str1 == str2:
        return len(set(str1)) < len(str1)    #Check for duplicate characters
    mismatches = [(a, b) for a, b in zip(str1, str2) if a != b]
    return len(mismatches) == 2 and mismatches[0] == mismatches[1][::-1]
    
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print(are_buddy_strings(str1, str2))