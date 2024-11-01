# Write a program to sort list in descending order

def desc_sort(num):
    return sorted(num, reverse = True)

num = [3,4,32,12,7,3]
print(desc_sort(num))