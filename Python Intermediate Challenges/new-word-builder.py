# Write a function to build a new word from the first two letters and the last two letters of a given word

def new_word_builder(word):

    result = ''
    result += word[:2] + word[-2:]

    return result

print(new_word_builder('challenge'))