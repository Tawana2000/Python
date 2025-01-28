# Write  a function to find the common elements between two lists

def find_common_elements(list1, list2):

    result = []

    for i in list1:
        if i in list2:
            result.append(i)

    return result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(find_common_elements(list1 , list2))