# Write a function to evaluate a ternary expression as string in condition ? true_result:false_result form

def evaluate_ternary(expression):

    condition, rest = expression.split('?')
    true_result, false_result = rest.split(':')
    return true_result.strip() if eval(condition.strip()) else false_result.strip()

print(evaluate_ternary("5 > 3 ? 'Yes' : 'No'"))
print(evaluate_ternary("2 == 3 ? 'Equal' : 'Not Equal'"))