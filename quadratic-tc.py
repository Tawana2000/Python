#An algorithm has quadratic time complexity if it's execution time is proportional to the square of the input size, this means if input increases, the time required to execute the program increases quadratically

def print_numbers(n):

    for i in range(n):
        for j in range(i):
            print(j)

print_numbers(3)