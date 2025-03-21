# Write a function to calculate the median of a stream of integers

import statistics
def calcualte_median(stream):

    medians = []
    temp = []

    for num in stream:
        temp.append(num)
        medians.append(statistics.median(temp))

    return medians

print(calcualte_median([1, 2, 3, 4, 5]))