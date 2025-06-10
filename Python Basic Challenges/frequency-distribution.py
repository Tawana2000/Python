# Write a function to create a frequency distribution of the elements in a list.

def frequency_distribution(lst):
    frequency = {}
    
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
            
    return frequency

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(frequency_distribution(lst))
