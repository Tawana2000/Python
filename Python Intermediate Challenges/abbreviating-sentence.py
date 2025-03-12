# Write a function to abbreviate a sentence by replacing each word with the first letter of the word and the length of the word

def abbreviate_sentence(sentence):

    return ' '.join(f"{word[0]}{len(word)}" for word in sentence.split())

print(abbreviate_sentence("Hello World"))