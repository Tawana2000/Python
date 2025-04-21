# Write a function to modify a tuple by adding an element at the end of it.

def modify_tuple(tupl, elem):

    tupl = list(tupl)
    tupl.append(elem)

    return tuple(tupl)
tupl = (1, 2, 3)
elem = 4
print(modify_tuple(tupl, elem))
