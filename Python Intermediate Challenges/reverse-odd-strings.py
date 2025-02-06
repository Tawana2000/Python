# Write a function to reverse all the words in a sentence that have odd length

def reverse_odd_length_words(sentence):
    words = sentence.split()
    result = [word[::-1] if len(word) % 2 != 0 else word for word in words]
    return " ".join(result)


sentence = "Hello world this is a test"
print(reverse_odd_length_words(sentence))