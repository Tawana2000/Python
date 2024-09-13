#Write a Python program to find the number of occurrences of each word in the string.
#Captain America is Captain of America
#{'captain': 2, 'america': 2, 'is': 1, 'of': 1}

def same_word_counter(string):

    counter = {}

    for word in string.split():

        word = ''.join([character.lower() for character in word if character.isalpha()])   #remove special character from the word and convert it to lowercase

        counter[word] = counter.get(word, 0) + 1      #if word is not in the counter dictionary, add it to the dictionary and if the word is already in a dictionary increment the value by 1 

    return counter 
    
string = input()
result = same_word_counter(string)
print(result)