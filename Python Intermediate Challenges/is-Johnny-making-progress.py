# Write a function to check if Johnny is making progress in his workout

def is_johnny_making_progress(day1, day2, day3):

    return day3 > day2 and day2 > day1

print(is_johnny_making_progress(1, 4, 3))