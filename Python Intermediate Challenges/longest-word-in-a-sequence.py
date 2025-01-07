# Write a function to find the longest word in a sequence
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

sentence = "The quick brown fox jumped over the lazy dog"
print(find_longest_word(sentence)) 
