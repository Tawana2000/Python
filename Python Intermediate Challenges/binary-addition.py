# Write a funcction to add two binary strings

def add_binary_strings(bin_str1, bin_str2):

    sum = bin(int(bin_str1, 2) + int(bin_str2, 2))

    return sum[2:]

print(add_binary_strings('1010', '1011'))