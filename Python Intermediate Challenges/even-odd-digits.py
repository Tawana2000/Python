# Write a function to count the number of even or odd digits in a list of integers

def count_digits(numbers, is_even):
    result = []
    
    for num in numbers:
        count = sum((int(digit) % 2 == 0) if is_even else (int(digit) % 2 != 0) for digit in str(abs(num)))
        result.append(count)
        
    return result

print(count_digits([1111, 2222], False))
print(count_digits([123, 456, 789], True))
