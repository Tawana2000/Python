# Write a function to check if two given lists are equal

def if_equal(lst1, lst2):

    return True if lst1 == lst2 else False

lst1 = list(map(int, input('Enter the list1 elements separated by space: ').split()))
lst2 = list(map(int, input('Enter the list2 elements separated by space: ').split()))

print(if_equal(lst1, lst2))