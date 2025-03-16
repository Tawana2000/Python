# Write a function to find the first Tuesday of the month

import datetime
def first_tuesday(month, year):

    day = 1
    while True:
        date = datetime.date(year, month, day)
        if date.weekday() == 1:       # 0 = Monday, 1 = Tuesday
            return date.strftime('%Y-%m-%d')
        
        day += 1

print(first_tuesday(1, 2025))