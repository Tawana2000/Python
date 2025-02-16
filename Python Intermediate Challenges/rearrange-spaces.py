# Write a function to rearrange spaces between words in a sentence so that they are evenly distributed

def rearrange_spaces(text):

    words = text.split()
    total_spaces = text.count(' ')

    if len(words) == 1:
        return words[0] + ' ' * total_spaces
    
    spaces_between =  total_spaces // (len(words) - 1)
    extra_space = total_spaces % (len(words) - 1)

    return (' ' * spaces_between).join(words) + ' ' * extra_space

print(rearrange_spaces(' This  is  a   sentence '))