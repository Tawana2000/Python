# Write a function to find the shortest word in a given string

def shortest_word(sentence):

    word = sentence.split()  # Split the sentence into words
    shortest = min(word, key = len)

    return shortest

sentence = 'This is an example sentence'
print(shortest_word(sentence))