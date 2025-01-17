# Write a function to find the highest integer in a list

def highest_integer(n):

    n = sorted(n)
    return max(n)

n = [3,5,62,4,12,45,23]
print(highest_integer(n))