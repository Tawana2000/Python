# Write a function to tye the given string using a broken keyboard
# The broken keyboard toggles the case of letters every time a vowel is pressed

def type_broken(word):

    vowel = 'aeiouAEIOU'
    result = []
    toggle_case = False

    for char in word:

        if char in vowel:
            toggle_case = not toggle_case

        if toggle_case:
            result.append(char.swapcase())

        else:
            result.append(char)

    return ''.join(result)

word = input('Enter the string: ')
print(type_broken(word))