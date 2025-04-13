# Write a function to find all words in a sentence that start with a vowel

def find_vowel_words(sentence):

    vowel = 'AEIOUaeiou'
    result = []
    words = sentence.split()
    for word in words:
        if word[0] in vowel:
            result.append(word)
    return result

sentence = 'Hello, how are you'
print(find_vowel_words(sentence))