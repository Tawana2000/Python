# Write a function to check if each card in the deck has exactly X copies

def is_x_of_a_kind(deck, x):

    return any(deck.count(card) >= x for card in set(deck))

deck = [1, 2, 3, 1, 2, 3]
x = 2
print(is_x_of_a_kind(deck, x))