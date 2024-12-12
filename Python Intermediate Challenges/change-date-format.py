# Write a function to convert a date from 'dd-mm-yyyy' format to 'mm-dd-yyyy' format

from datetime import datetime
def convert_date_format(date_str, current_format, desired_format):


    try:

        date_object = datetime.strptime(date_str, current_format)

        return date_object.strftime(desired_format)
    
    except ValueError:
        return 'Invalid date or format'
    

current_date = "08-11-2018"
current_format = "%d-%m-%Y"
desired_format = "%Y/%m/%d"

print(convert_date_format(current_date, current_format, desired_format))