# Write a function to split a list into chunks of a specified size

def chunk_list(lst, n):

    result = []

    for i in range(0, len(lst), n):
        result.append(lst[i:i + n])

    return result

print(chunk_list([1, 2, 3, 4, 5], 2))