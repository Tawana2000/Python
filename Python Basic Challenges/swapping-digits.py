# Write a function to check if swapping the digits of a two digit number does not result in a larger number

def largest_swap(num):

    num = str(num)
    swapped_num = num[::-1]

    return int(swapped_num) < int(num)

print(largest_swap(27))

