# Write a function to validate a solution
#  The function should take two inputs, proposed_solution and the correct solution, if proposed solution is correct return 'Correct', if not, return 'Incorrect'

def validate_solution(proposed_solution, correct_solution):
    return 'Incorrect' if proposed_solution != correct_solution else "Correct"

proposed_solution = input("What is the proposed solution: ")
correct_solution = input("What is the correct solution: ")
print(validate_solution(proposed_solution, correct_solution)
