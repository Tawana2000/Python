# An algorithm has linear TC if the execution time is proportional to the size of the input, this means if the input increases, the TC also increases linearly

def print_hello(n):

    for i in range(n):    # n
        print('Hello')    # n
                          # So TC = (2n), this means if the input is 5, 2*5 statements will be executed, ignoring the coefficient. the TC = O(n)
print_hello(5)            

