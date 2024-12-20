# Write a function to count the occurence of each word in a given list of words

def word_order(words):

    result = {}

    for word in words:
        if word in result:
            result[word] += 1

        else:
            result[word] = 1

    return result

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_order(words))
