# Write a function to find the mth smallest value in K sorted lists.

def find_mth_smalles(list, m):

    result = []
    for i in list:
        result.extend(i)
    return result[m - 1]

print(find_mth_smalles([[9, 10], [11, 12], [13, 14]],
3))
