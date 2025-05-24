# Write a function to find the longest consecutive zeroes in a binary string
def longest_zeroe_sequence(binary_string):
    max_count = current_count = 0

    for char in binary_string:
        if char == '0':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

print(longest_zeroe_sequence("1001000100001000"))