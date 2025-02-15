# Write a function to extend the vowels in a string

def extend_vowels(string, n):

    vowels = "AEIOUaeiou"
    result = []

    for char in string:
        if char in vowels:
            result.append(char * n)

        else:
            result.append(char)

    return ''.join(result)

print(extend_vowels('hello', 3))