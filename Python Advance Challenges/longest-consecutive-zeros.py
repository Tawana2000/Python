# Write a program to find the longest sequence of consecutive zeros in a binary string

def longest_zeros_sequence(binary_string):

    max_count = 0
    current_count = 0

    for char in str(binary_string):
        if char == '0':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

print(longest_zeros_sequence(101001000100001))