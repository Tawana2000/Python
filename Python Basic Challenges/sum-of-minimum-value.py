# Write a function to calculate the sum of the  minimum value in each row of a 2D list

def sum_of_min_values(lst):

    return sum(min(row) for row  in lst)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_of_min_values(lst))
