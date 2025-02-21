# Write a function to calculate the earned run average (ERA) in baseball

def calculate_era(earned_runs, innings_pitched):

    era = (earned_runs * 9) / innings_pitched
    return round(era, 2)

print(calculate_era(3, 9))