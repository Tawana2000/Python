# Write a function to count the number of occurrences of an item in a tuple

def count_occ(item, tup):

    count = 0

    for i in tup:
        if i == item:
            count += 1

    return count

tup = ('a','b','a','c','d','a')
item = input("Enter the item to search in tuple: ")
print(count_occ(item, tup))