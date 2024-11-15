# Write a function to return the first and last parameter passed to a function as a tuple

def first_last(*args):

    result = []

    if args:
        result.append(args[0])
        result.append(args[-1])
    return tuple(result)
    
args = [1, 2, 3, 4, 5]
print(first_last(*args))