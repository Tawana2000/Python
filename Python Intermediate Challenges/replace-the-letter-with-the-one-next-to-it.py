# Write a function to change every letter in a given string to the next letter in the alphabet

def shift_to_next_letter(s):
    result = []
    
    for char in s:
        if char.isalpha():
            if char.islower():
                result.append(chr(((ord(char) - ord('a') + 1) % 26) + ord('a')))
            elif char.isupper():
                result.append(chr(((ord(char) - ord('A') + 1) % 26) + ord('A')))
        else:
            result.append(char)
    
    return ''.join(result)

input_string = "Hello World!"
output_string = shift_to_next_letter(input_string)
print(output_string) 

