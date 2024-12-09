# Write a function to convert bird names into four letter bird codes

def bird_code(name):

    words = name.split()

    if len(words) == 1:
        return words[0][:4]
    
    elif len(words) > 1:
        return ''.join(word[:2].upper() for word in words)


name = 'Northern Cardinal'

print(bird_code(name))