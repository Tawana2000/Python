# Write a function to find the date of the first Tuesday of a given month and year

import datetime
def first_tuesday(month, year):

    date = datetime.date(year, month, 1)

    while date.weekday() != 1:
        date += datetime.timedelta(days = 1)

    return date.strftime('%Y-%m-%d')

month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

print(first_tuesday(month, year))