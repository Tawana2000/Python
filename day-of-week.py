# Write a function to return the day of the week, given an integer
# for the input 3, the output should be Wednesday

def check_day(n):

    days = {1: "Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"}

    return days.get(n)

n = 3
print(check_day(n))