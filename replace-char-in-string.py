#Write a function to replace all vowels in a string with a secified character

def replace_vowels(string, char):

    vowels = 'aeiouAEIOU'
    result = ''

    for i in string:
        if i in vowels:
            result += char

        else:

            result += i

    return result

string = 'hello world'
char = input('Enter the charater to swapp with string vowel characters: ')

print(replace_vowels(string, char))
