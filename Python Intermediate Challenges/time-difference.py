# Write a function to calculate the duration in minutes between a starting time and a final time

def calculate_duration(start_time, final_time):

    h1, m1 = map(int, start_time.split(":"))
    h2, m2 = map(int, final_time.split(":"))

    return abs((h2 - h1) * 60 + (m2 - m1))

print(calculate_duration("14:30", "16:00"))