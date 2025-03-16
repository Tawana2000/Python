#  Write a function to solve the Busy Beaver problem

def busy_beaver(n):

    if n == 1:
        return 1
    return busy_beaver(n - 1) * 2 + 2

print(busy_beaver(3))