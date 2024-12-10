# Write a function to determine if the 13th day of agiven month and year falls on a Friday

from datetime import datetime
def is_friday_13(month, year):

    try:

        date = datetime(year, month, 13)
        return date.weekday() == 4
    
    except ValueError:
        return False
    

month = int(input('Enter the month (1-12): '))
year = int(input('Enter the year: '))

if is_friday_13(month, year):
    print(f"The 13th of {month}/{year} falls on a Friday!")

else:
    print(f"The 13th of {month}/{year} does not fall on a Friday.")