# Write a function to reverse a given list 

def reverse_list(lst):

    return lst[::-1]

lst = list(map(int, input("Enter the list elements separated by space: ").split()))
print(reverse_list(lst))