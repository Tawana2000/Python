# Write a function to calculate bonus from an employee's salary
# An employee gets a 5% bonus if they have worked for over 5 years

def calculate_bonus(salary, years):

    bonus = 1

    if years <= 5:
        return "Not eligible for bonus"
    

    bonus = (5 * salary) / 100

    return bonus

salary = 50000
years = 6

print(calculate_bonus(salary, years))