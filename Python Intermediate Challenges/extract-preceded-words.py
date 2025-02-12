# Write a function to extract all the words that are preceded by the word 'Python' n a given text

def extract_words(text):

    words = []
    text_list = text.split()

    for i in range(len(text_list) - 1):
        if text_list[i] == "Python":
            words.append(text_list[i + 1])
    
    return words

text = "I love Python programming. Python is great for data science. Python developers are in demand."
print(extract_words(text))