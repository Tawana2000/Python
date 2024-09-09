#Create a Python program to print the duplicate elements in a list.

my_list = [2, 'python', 5, 7, 'python', 'java', 5]

my_set = set(my_list)

repeated = []

for items in my_set:
    if my_list.count(items) > 1:
        repeated.append(items)

print(repeated)