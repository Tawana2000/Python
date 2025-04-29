# Write a function to find the most common character in a given string

def most_common_character(s):

    if not s:
        return None
    
    return max(s, key = s.count)

print(most_common_character('Hello World'))