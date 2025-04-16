# Write a function to find all negative numbers within a given range

def find_negative(start, end):
    
    numbers = []
    for i in range(start, end):
        
        if i < 0:
            numbers.append(i)
        i += 1

    return numbers

start  =-5
end = 5

print(find_negative(start, end))
