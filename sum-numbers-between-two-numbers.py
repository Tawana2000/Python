# Write a function to calculate the sum of all numbers between two given numbers

def sum_of_digits(start, end):

    sum = 0
    for i in range(start, end + 1):
        sum += i

    return sum

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print(sum_of_digits(start, end))