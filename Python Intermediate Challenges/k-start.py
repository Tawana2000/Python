# Write a function to extract all words that start with the letter K from a list of strings

def extract_k_words(words):

    result = []

    for i in words:
        if i[0] == 'K' or i[0] == 'k':
            result.append(i)

    return result
words = ['Kite', 'Kangaroo', 'Kiwi', 'Apple', 'Banana']
print(extract_k_words(words))