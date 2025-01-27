# Write a funtion to check if a list contains at least two distinct elements 

def check_distinct(lst):

    for i in range(1, len(lst)):

        if abs(lst[i] != lst[i - 1]):
            return True
        
    return False

print(check_distinct([1,1,1,3]))