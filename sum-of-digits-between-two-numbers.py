# Write a program to calculate the sum of all digits between two given numbers

def cal_sum(start, end):
    result = 0

    for n in range(start, end + 1):
        for digits in str(n):
            result += int(digits)
    return result

start = int(input('Enter the start number: '))
end = int(input('Enter the ending number: '))

print(cal_sum(start, end))
