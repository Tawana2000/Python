# Write a function to calculate the difference between two given dates in years, months, and days

from datetime import datetime
def date_difference(date1,date2):

    date_obj_1 = datetime.strptime(date1, "%Y-%m-%d")
    date_obj_2 = datetime.strptime(date2, "%Y-%m-%d")

    diff = date_obj_1 - date_obj_2
    years = diff.days // 365
    months = (diff.days % 365) // 30
    days = (diff.days % 365) % 30

    return f"{years} years, {months} months, {days} days"

date1 = '2022-12-31'
date2 = '2000-01-01'

print(date_difference(date1, date2))
