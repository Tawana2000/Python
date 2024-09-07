#Create a Python program to print the numbers that come immediately before and after a given number.

def check_before_after(n):

    before = n - 1

    after = n + 1

    return (before,n,after)

print(check_before_after(5))