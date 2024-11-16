# Write a function to count the number of arguments passed to a function

def count_arg(*args):

    count = 0

    for i in args:
        count += 1

    return count
args = map(int, input().split())
print(count_arg(*args))