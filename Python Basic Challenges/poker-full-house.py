# Write a function to check if a given hand of poker cards is a full house
# of poker, a full house is when you have three of one kind and two of another
from collections import Counter
def is_full_house(hand):
    counts = Counter(hand).values()
    return sorted(counts) == [2, 3]

print(is_full_house(['2', '2', '3', '3', '3']))