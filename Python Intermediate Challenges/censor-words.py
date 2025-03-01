# Write a function to censor words that are longer than four characters in a sentence

def censor_words(sentence):
    
    result = []

    for word in sentence.split():

        if len(word) > 4:
            result.append('*' * len(word))

        else:
            result.append(word)

    return ' '.join(result)
    
print(censor_words('I love programming in Python'))