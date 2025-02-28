# Write a function to sort a string based on its last character

def sort_string(s):

    words = s.split()
    sorted_words = sorted(words, key=lambda word: word[-1])
    return ' '.join(sorted_words)

sentence = "hello world this is python"
result = sort_string(sentence)
print(result)