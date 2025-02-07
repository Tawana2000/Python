# Write a function to generate all the permutation of a string

def generate_permutation(s):

    result = []

    if len(s) == 1:
        return [s]
    
    for item, char in enumerate(s):
        for perm in generate_permutation(s[:item] + s[item + 1:]):
            result.append(char + perm)

    return result

s = "CSE"
print(generate_permutation(s))
