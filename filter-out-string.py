# Write a function to filter out all the strings from a list

def filter_strings(lst):

    new_lst = []

    for items in lst:

        try:
            new_lst.append(int(items))

        except ValueError:
            continue

    return new_lst

lst = [1, 'a', '2', 'b', 3]

print(filter_strings(lst))