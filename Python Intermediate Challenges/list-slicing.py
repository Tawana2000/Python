# Write a function to create a new list from an existing list using list slicing

def list_slicing(lst, start_index, end_index):


    return lst[start_index: end_index]

lst = [1,2,3,4,5]
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index :"))

print(list_slicing(lst, start_index, end_index))