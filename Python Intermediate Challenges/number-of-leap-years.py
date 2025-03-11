# Write a function to calculate the number of leap years between two given years

def count_leap_years(start_year, end_year):

    count = 0

    for year in range(start_year, end_year + 1):

        if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
            count += 1

    return count

print(count_leap_years(2000, 2020))