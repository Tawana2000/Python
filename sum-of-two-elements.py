#Create a Python program to find all the combinations of list elements whose sum equals the target value.


def find_sum(num_list, target):

    temp_list = [] # to avoid duplicates

    for i in num_list:

        if (target - i) in temp_list:
            print(target - i, i)

        temp_list.append(i)


num_list = numbers = [1, 5, 6, 3, 2, 4]
target = 7
find_sum(num_list, target)