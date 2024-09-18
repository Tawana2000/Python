#In any given string of size n, find all the words that start with the given letter. The output must be case insensitive.

def initial(string, letter):

    result_list = []
    words = string.split()  #split strings into words

    for items in words:
        if items[0].lower() == letter.lower():
            result_list.append(items)

    return result_list

string = input()
letter = input()
print(initial(string, letter))