# Write a function to decipher a given string using a given key

def decipher_string(text, key):

    deciphered = ''.join(chr(ord(c) - key) for c in text)
    return deciphered

print(decipher_string("hij", 2))