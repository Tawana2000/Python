#Create a Python program to encrypt a string by shifting the alphabets by 1, for ex: input = hello world, output should be: ifmmp xpsme

def encrypt(character):
    
    #if character is z assign it to a
    if character == 'Z':
        secret = 'A'
    
    elif character == 'z':
        secret = 'a'
    
    else:
        secret = chr(ord(character) + 1)
    
    return secret


def main(string):

    result = ''  #encrypted string

    for character in string:

        if character.isalpha():  #if character is alphabet, call the encrypt function and concat the outcome to the result
            result += encrypt(character)


        else:     #if character is not an alphabet, concat the character as it is to result
            result += character

    return result

encrypted_string = main('i am lazy')
print(encrypt)

encrypted_string = main('I AM LAZY')
print(encrypt)