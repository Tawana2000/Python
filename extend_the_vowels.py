#In any given string, repeat the vowel letters up to a given number.

def extend(string, n):

    vowels = 'aeiou'
    new_str = ''

    for char in string:
        if char.lower() in vowels:
            new_str += char * n

        else:
            new_str += char
    
    return new_str


string = input()
n = int(input())
print(extend(string, n))