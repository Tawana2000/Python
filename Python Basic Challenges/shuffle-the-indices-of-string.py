# Write a function to shuffle the indices of a string

def index_shuffle(txt):

    even_index = ''
    odd_index = ''

    for i in range(len(txt)):
        if i % 2 == 0:
            even_index += txt[i]
        else:
            odd_index += txt[i]

    return even_index + odd_index

print(index_shuffle('abcdef'))