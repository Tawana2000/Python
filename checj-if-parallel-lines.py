# Write a function to check if two lines are parallel based on their slopes

def are_paralle(m1, m2):

    return True if m1 == m2 else False

m1 = int(input('Enter the slope for m1: ' ))
m2 = int(input('Enter the slope of second line: '))

print(are_paralle(m1, m2))
