# Write a function to calculate the number of days between two given dates

from datetime import datetime
def calculate_days(date1, date2):

    date_format = "%Y-%m-%d"

    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)

    return abs((d2 - d1).days)

print(calculate_days("2022-01-01", "2022-01-31"))
print(calculate_days("2024-03-15", "2025-08-24"))