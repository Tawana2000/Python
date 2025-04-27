# Write a function to copy specific elements from one tuple to a new tuple

def copy_elements(original_tuple, indices):

    return tuple(original_tuple[i] for i in indices)
    
original_tuple = (1, 2, 3, 4, 5)
indices = [0, 2, 4]
print(copy_elements(original_tuple, indices))