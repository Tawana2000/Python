# Write a function to calculate the difference between two given dates in years, months, and days

from datetime import datetime
def date_difference(date1, date2):

    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')

    if d1 > d2:
        d1, d2 = d2, d1

    years = d2.year - d1.year
    months = d2.month - d1.month
    days = d2.day - d1.day

    if days < 0:
        months -= 1
        days += (d1.replace(month = d1.month + 1, day = 1) - d1).days

    if months < 0:
        years -= 1
        months += 12

    return f"{years} years, {months} months, {days} days"

date1 = '2022-12-31'
date2 = '2000-01-01'
print(date_difference(date1, date2))