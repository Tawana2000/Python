# Write a function to check if the last item of a list is the same as the concatenation of all other items in the list.

def match_last_item(lst):

    return ''.join(lst[:-1]) == lst[-1]

lst = ['abc', 'def', 'ghi', 'abgdefghi']
print(match_last_item(lst))