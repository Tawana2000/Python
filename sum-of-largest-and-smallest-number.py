#From the given list of numbers, find the sum of the largest and the smallest element.
#we can use min() and max() also to find the smallest and largest number 

def sum_min_max(list1):

    length = len(list1)
    list1.sort()

    print(list1[length-1] + list1[0])

list1 = [12,34,2,345,8,41]
sum_min_max(list1)
