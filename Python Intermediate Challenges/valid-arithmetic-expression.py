# Write a function to check if a given string is a valid arithmetic expression 

def is_math_expression(s):

    valid_items = set("0123456789+-*/().")

    return all(char in valid_items for char in s)
    
s = '234/13'
print(is_math_expression(s))

s = 'vd14435'
print(is_math_expression(s))