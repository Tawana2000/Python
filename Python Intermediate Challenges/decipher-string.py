# Write a function to decipher a given string using a given key

def decipher_string(input_string, shift_key):
    result = ''
    for char in input_string:
        # Shift the character backward by the given key value, wrapping around within 'a' to 'z'
        new_char = chr((ord(char) - ord('a') - shift_key) % 26 + ord('a'))
        result += new_char
    return result


input_string = input("Enter the string to decipher: ").lower()
shift_key = int(input("Enter the shift key: "))


print("Deciphered string:", "'" + decipher_string(input_string, shift_key) + "'")
