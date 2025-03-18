# Write a function to combine two lists and return a list of consecutive integers from the minimum to the maximum number inclusive

def consecutive_sequence(list1, list2):

    combined = sorted(list1 + list2)
    
    if len(combined) < 2:
        return "Not Consecutive"
    
    is_consecutive = True
    for i in range(len(combined) - 1):
        if combined[i + 1] - combined[i] != 1:
            is_consecutive = False
            break
    
    if is_consecutive:
        return combined
    else:
        return "Not Consecutive"

# Test cases
print(consecutive_sequence([1, 2, 3], [4, 5, 6]))
print(consecutive_sequence([1, 2, 4], [4, 5, 6])) 
print(consecutive_sequence([10], [12]))           
print(consecutive_sequence([7, 8], [9]))