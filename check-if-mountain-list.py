# Write a function to determine if a list is a valid mountain list
# A valid mountain list is a list that first strictly increases to a peak and then strictly decreases

def is_mountain(lst):
    
    if len(lst) < 3:
        return False
    
    i = 0

    while i + 1 < len(lst) and lst[i] < lst[i + 1]:   #Ascending part: strictly increasing
        i += 1

    if i == 0 or i == len(lst) - 1:  #The cannot be the first or last element
        return False
    
    while i + 1 < len(lst) and lst[i] > lst[i + 1]:   #Descending part: stricly decreasing
        i += 1

    return i == len(lst) - 1    #If we traversed the entire array, it's a mountain
        
lst = list(map(int, input("Enter the list items to check: ").split()))
print(is_mountain(lst))