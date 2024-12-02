# Write a function to count the number of parameters passed to a function

def count_parameters(*args):
     
     return len(args)

print(count_parameters(1, 3, 6, 8))