#Given a string, only reverse the words that have an odd length of characters in a string.

def odd_reverse(string):

    words_list = string.split()   #break the string into list of words

    new_string = []


    for word in words_list:

        if len(word) % 2 == 1:
            new_string.append(word[::-1])

        else:

            new_string.append(word)

    return ' '.join(new_string)


string = input()
print(odd_reverse(string))