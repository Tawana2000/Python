# Write a function to find and return the digits that are shared between two given numbers

def shared_digits(num1, num2):
    
    result = []

    for num in str(num1):
        if num in str(num2):
            result.append(num)

    return sorted(list(set(result)))

print(shared_digits(12345, 64835))