# Write a function to calculate the sum of all digits in a given number

def cal_sum(number):
    
    result = 0

    for i in str(number):
        result += int(i)
    
    return result

print(cal_sum(34))
