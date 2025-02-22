# Write a function to calculate the total time spent washing hands
# Asuming you are washing hands everyday and it takes 21 sec

def total_washing_time(times_per_day, months):
    total_seconds = 30 * months * times_per_day * 21 
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes} minutes and {seconds} seconds"

print(total_washing_time(8, 7))