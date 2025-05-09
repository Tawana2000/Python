# Write a function to count the total number of elements in a multi-dimensional list

def count_elements(lst):

    count = 0

    for i in range (len(lst)):

        for j in range(len(lst[i])):
            count += 1


    return count

lst = [[1, 2], [3, 4], [5, 6]]
print(count_elements(lst))
