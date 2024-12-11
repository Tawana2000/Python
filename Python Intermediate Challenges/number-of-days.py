# Write a function to calculate the number of days between two given dates

from datetime import datetime
def days_spent_together(date1, date2):

    try:

        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        delta = abs((d2 - d1).days)
        return delta
    
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."
    

date1 = input('Enter the first date (YYYY-MM-DD): ')
date2 = input('Enter the second date (YYYY-MM-DD): ')

result = days_spent_together(date1, date2)

if isinstance(result, int):
    print(f"The number of days between {date1} and {date2} is {result} days.")

else:
    print(result)