#find the majority element from the given list of size n.

def majority_element(num_list):

    for num in num_list:

        count = num_list.count(num)

        if count > len(num_list) // 2:
            return num
        
number = [1,7,8,7,7,7]
number = [5, 2, 6, 6, 8, 12, 23, 23, 8, 8]
print(majority_element(number))
