# Write a function to check if the number of unique positive numbers is greater than the number of unique negative numbers in a list
# For the input [-1, -1, -2, -3, 4, 4], Ouput should be False

def positive_dominant(lst):

    count_positive = 0
    count_negative = 0

    for i in lst:
        if i > 0:
            count_positive += 1
        else:
            count_negative += 1

    if count_positive > count_negative:
        return True
    else:
        return False
    
lst = [-1, -1, -2, -3, 4, 4]
print(positive_dominant(lst))