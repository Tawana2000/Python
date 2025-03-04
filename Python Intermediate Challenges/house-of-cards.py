# Write a function to calculate the number of cards needed to build a house of cards with n floors

def cards_needed(n):

    return round(n * ( 3 * n + 1) / 2)

print(cards_needed(3))