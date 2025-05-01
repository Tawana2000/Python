# Write a function to calculate the time save by speeding

def time_saved(distance, speed1, speed2):

    time1 = distance / speed1
    time2 = distance / speed2

    less_time = min(time1, time2)
    more_time = max(time1, time2)

    return round((more_time - less_time), 2)

print(time_saved(400, 80, 100))