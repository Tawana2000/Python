#Create a Python program to find a missing number from a list.
# To solve this 1. find the size of the list (n), 2. find the sum of the sequence ((n + 1) * (n + 2) / 2), 3. find the sum of all elements present in the list, 4. sum of sequence - sum of elements present in the list

def missing(list1):

    length = len(list1)
    sum_sequence = ((length + 1) * (length + 2) // 2)
    sum_elements = sum(list1)

    missing_number = sum_sequence - sum_elements
    return missing_number

list1 = [1, 3, 4, 5, 6, 7, 8, 9, 10]
print(missing(list1))