#Q3.Encrypting a message by adding a key value to every character 

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
text = input("Enter a string:")
s = int(input("Enter a number:"))
print("Text:" +text)
print("Shift:" +str(s))
print("Cipher:" +encrypt(text,s))
