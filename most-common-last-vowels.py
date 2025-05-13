#You are given a string that contains multiple words. Now write a Python program that counts the most common vowel that words end with.

def count_common_vowels(string):

    vowels = 'aeiou'
    word = string.split() #break string into list of words
    counter = {}

    for item in word:

        if item[-1] in vowels:      #if last letter of the word is in vowels
            counter[item[-1]] = counter.get(item[-1], 0) + 1

    max_ended = max(counter.values())

    for key, value in counter.items():

        if value == max_ended:
            return key
        
string = input()
print(count_common_vowels(string))
