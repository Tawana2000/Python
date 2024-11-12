# Write a function to check if the sum of two numbers is less than a third number

def sum_check(n1, n2, n3):
    
    return True if n1 + n2 < n3 else False

n1, n2, n3 = map(int, input('Enter three numbers separated by spaces: ').split())
print(sum_check(n1, n2, n3))
