# Write a function to calculate the weekly salary of an employee
# The employee earns $20 per hour for the first 40 hours and $25 for every hour after that

def calculate_salary(hours):

    overtime_hours = hours - 40

    return (40 * 20) + (overtime_hours * 25)

print(calculate_salary(45))