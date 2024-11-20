# Write a function to repeat the same item multiple times in a list

def repeat_item(item, n):

    result = []
    result.append(item)
    result *= n

    return result

print(repeat_item('a', 5))