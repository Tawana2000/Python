# Write a function to find the longest daily streak of a habit

def longest_habit_streak(habits):
    longest_streak = current_streak = 0

    for day in habits:
        if day:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0

    return longest_streak


habits = [True, True, False, True, True, True]
print("Longest Streak:", longest_habit_streak(habits))