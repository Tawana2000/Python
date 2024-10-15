""" Write a function to find the number that occurs twice and the number that is missing from a sequence of numbers from 1 to n.
for the imput [1,2,2,4] the output should be [2,3] """

def find_mismatch(nums):
    
    my_set = set(nums)

    new_list = [] #to store the duplicate items

    for items in my_set:
        if nums.count(items) > 1:
            new_list.append(items)

    
    lenght = len(my_set)
    sum_seq = ((lenght + 1) * (lenght + 2) // 2)
    sum_elements = sum(my_set)
    missing_number = sum_seq - sum_elements
    new_list.append(missing_number)
    return new_list
nums = []

for i in range (0, len(nums)):
    number = int(input())
    nums.append(number)
print(find_mismatch(nums))
