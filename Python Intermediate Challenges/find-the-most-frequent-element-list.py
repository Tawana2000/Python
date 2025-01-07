# Write a function to find the most frequent element in a list, if there is a tie, return any one of the most frequent elements

from collections import Counter

def most_frequent(lst):
    if not lst:
        return None
    count = Counter(lst)
    return max(count, key=count.get)

lst = [1, 3, 3, 2, 1, 3, 4, 1]
print(most_frequent(lst))
