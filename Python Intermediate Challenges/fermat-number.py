# Write a function to calculate the Fermat number for a given index

def fermat_number(n):

    fn = 2 ** (2 ** n) + 1
    return fn

print(fermat_number(3))