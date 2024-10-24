#An algorithm has logarithmic TC if execution time is proportional to the logarithm of the imput size, that mean, if the input size increases, the number of steps required to complete the program grows very slowly

def print_numbers(n):
    i = 1

    while i < n:
        print(i)

        i = i * 2

print_numbers(5)