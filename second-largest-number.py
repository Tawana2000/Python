#create a Python program to find the second-largest number from the list.

def second_largest(list1):

    new_list = list(set(list1))
    new_list.sort()
    
    print(new_list[-2])

list1 = [4, 51 , 5, 6, 2, 51, 23]

second_largest(list1)