# Write a function to calculate the probability of selecting the letter 'a' from a given string

def probability_of_a(s):

    return round(s.count('a') / len(s), 2)

print(probability_of_a('banana'))