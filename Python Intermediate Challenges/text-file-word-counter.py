# Write a function that reads a text file and counts the number of words in it

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

print(count_words_in_file('sample.txt'))
