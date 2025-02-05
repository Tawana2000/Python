# Write a function to return positive numbers from a list

def filter_positive(lst):

    result = []

    for num in lst:
        if num > 0:
            result.append(num)
    
    return result

lst = [5, 3, -2, 1, 0]
print(filter_positive(lst))