# Write a function to add an item to the end of the list

def append_item(lst, item):

    lst.append(item)
    return lst

lst = ['apple', 'Pear', 'Grape', 'Kiwi']
item = 'banana'

print(append_item(lst, item))