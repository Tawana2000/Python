# Write a function to check if a given list is special or not
# A list is special if every element at an even index is even and every element at an odd index is odd

def is_special_list(lst):
    
    return all(lst[i] % 2 == i % 2 for i in range(len(lst)))

print(is_special_list([2, 1, 4, 3, 6])) 
print(is_special_list([2, 3, 4, 6]))