# Write a function to determine the number of solutoins a quadratic equation has
# A quadratic equation is in the form ax^2 + bx + c = 0, the discriminant is calculated as b^2 - 4ac. If the discriminant is greater than zero, there are two solutions. If its equal to zero, there's one solution. If it's less than zero, there are no real solutions

def quadratic_solutions(a, b, c):

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    else:
        return 0
    
print(quadratic_solutions(1, -3, 2))