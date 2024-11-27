# Write a function to evaluate an expression represented as string and return its value

def evaluate_expression(expression):

    try:

        result = eval(expression)
        return result
    
    except Exception as e:
        return f"Error: {e}"

expression = '2 + 3 * 4 - 5'
print(evaluate_expression(expression))