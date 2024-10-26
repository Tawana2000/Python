# Time complexity for the following code

def print_number(n):

    for i in range(n):            # n
        print(i)                  # n

    for j in range(n):            # n
        print(j)                  # n
 
print_number(5)                   # result = 4n

# so time complexity = O(n) because the two loops are independent of each other