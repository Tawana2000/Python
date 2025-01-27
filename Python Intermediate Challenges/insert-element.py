# Write a function to insert an element at a given location in a list

def insert_element(lst, index, value):

    lst.insert(index, value)
    return lst

lst = [4,5,7]
index = 1
value = 4
print(insert_element(lst, index, value))