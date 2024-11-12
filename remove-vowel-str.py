# Write a function to remove all vowels in a string

def remove_vow(string):

    vowel = 'aeiouAEIOU'
    result = ''

    for i in string:
        if i not in vowel:
            result += i

    return result

string = 'Hello, I am happy to be here'
print(remove_vow(string))