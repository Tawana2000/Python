#Given a non-empty string, print all the permutations of that string.
#Permutation refers to the different ways elements from a set can be arranged, for ex: pan --> pna, anp, apn ... 

def get_permut(string, i = 0):
    if i == len(string):
        print(''.join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
        words[i], words[j] = words[j], words[i]

        get_permut(words, i + 1)

get_permut('pan')