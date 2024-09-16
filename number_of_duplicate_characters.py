#Write a Python program to count the number of characters that occur more than once in a string.

def count_character(sentence):

    counter = 0

    duplicate_character = ''


    for character in sentence:

        if character.isalpha():


            if sentence.count(character) > 1 and character not in duplicate_character:

                counter += 1

                duplicate_character += character

    return counter


sentence = input()
print(count_character(sentence))