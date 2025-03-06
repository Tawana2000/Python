# Write a function to calculate the time when two friends will meet if they start at different times and maintain constant speeds
"""
- Each tuple contains the start times (in hours) and speeds (in km/hr) of the two friends 
- Return the meeting time in hours, rounded off to two decimal places
- The distance traveled by each friend is calculated as speed * time. The friends meet when their distances are equal. Solve for time in this equation to find the meeting time
"""

def meeting_time(friend1, friend2):

    x1,y1=friend1
    x2,y2=friend2
    return round(abs(x1 - x2) / (y1 + y2), 2)


print(meeting_time((0, 3), (10, 2)))
print(meeting_time((2, 5), (4, 10)))
print(meeting_time((0, 5), (10, 5)))
