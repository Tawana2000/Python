#Create a Python program to sort the words in a string alphabetically.

sentence = 'python is easy'

words = sentence.split()

words.sort()

for word in words:
    print(word)