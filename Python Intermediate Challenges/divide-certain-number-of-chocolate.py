# Write a function to divide a certain number of chocolates among a group of children

def divide_chocolates(chocolates, children):

    
    if chocolates <= 0:
        raise ValueError ("Oops, No chocolates available.")
    if children <= 0:
        raise ValueError ("Looks like children are absent.")
    
    no_chocolates = chocolates // children
    remainder = chocolates % children

    return f"Each child gets {no_chocolates} chocolates. Remaning: {remainder}"

chocolates = int(input("Enter the number of chocolates available: "))
children = int(input("How many children: "))

print(divide_chocolates(chocolates, children))

"""
try:

    chocolates_per_child, remainder = divide_chocolates(chocolates, children)
    print(f"Each child gets {chocolates_per_child} chocolates.")
    print(f"Remaining: {remainder}")

except ValueError as error:
    print(error)
"""