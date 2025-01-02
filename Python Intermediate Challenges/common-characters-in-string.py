# Write a function to find the three most common characters in the given string

def find_common_chars(string):

    char_count = {}

    if not string:
        raise ValueError("The input string is empty!")
    
    for index, char in enumerate(string):
        if char not in char_count:
            char_count[char] = [0, index]
            
        char_count[char][0] += 1
        
    sorted_chars = sorted(char_count.items(), key = lambda x: (-x[1][0], x[1][1]))

    return [(char, count[0]) for char, count in sorted_chars[:3]]

string = "hello world"
print(find_common_chars(string))