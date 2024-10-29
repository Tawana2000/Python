# Write a function to calculate the mean of all digits

def mean_of_digits(number):
    digits = [int(digit) for digit in str(abs(number))]  # Convert number to a list of digits
    return sum(digits) / len(digits) if digits else 0     # Calculate mean

# Example usage
number = 12345
print("Mean of digits:", mean_of_digits(number))