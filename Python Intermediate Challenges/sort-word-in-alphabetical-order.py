# Write a function to sort words in alphabetical order

def sort_words(sentence):
    words = sentence.split()
    return sorted(words, key=str.lower)

sentence = "Banana apple Orange grapes"
print(sort_words(sentence))
