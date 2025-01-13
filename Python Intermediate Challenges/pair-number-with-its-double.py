# Write a function to create a dictionary that pairs each number with its double

def max_pairs(n):

    result = {}

    for i in range(1, n + 1):
        result[i] = 2 * i
    

    return result

n = 5
print(max_pairs(n))