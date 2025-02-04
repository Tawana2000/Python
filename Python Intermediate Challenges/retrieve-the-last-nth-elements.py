# Write a function to retrive the last 'n' elements from a list

def retrive_last_elements(lst, n):

    return lst[-n:] if n <= len(lst) else lst

lst = [1, 2, 3, 4, 5]
n = 2

print(retrive_last_elements(lst, n))
