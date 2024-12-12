# Write a function to calculate the Jacobsthal number of a given index

def jacobsthal(n):

    if n < 0:
        return 'Please enter a positive number!'
    
    if n == 0:
        return 0
    
    elif n == 1:
        return 1

    return jacobsthal(n - 1) + 2 * jacobsthal(n - 2)

n = int(input('Enter the number to find the Jaconsthal value of it: '))
print(jacobsthal(n))