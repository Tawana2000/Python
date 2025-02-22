# Write a function to record the highest and lowest temperature for a week

def record_temperature(temps):

    result = []
    result.append(max(temps))
    result.append(min(temps))

    return result

temps = [20, 22, 23, 24, 25, 26, 27]

print(record_temperature(temps))