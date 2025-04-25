# Write a function to find the largest number that can be formed by swapping two digits of a given number

def largest_swap(num):

    num = str(num)
    swapped = num[::-1]

    return int(swapped) if swapped > num else num

print(largest_swap(27))