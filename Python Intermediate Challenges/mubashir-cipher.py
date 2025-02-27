# Write a function to implement the Mubashir Cipher

def mubashir_cipher(text):

    return "".join(chr(219 - ord(c)) if c.isalpha() else c for c in text.lower())

print(mubashir_cipher('abc'))