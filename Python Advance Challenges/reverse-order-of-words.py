# Write a function to reverse the order of words in a given string

def reverse_words(s):

    return ' '.join(s.split()[::-1])

print(reverse_words('Hello World'))