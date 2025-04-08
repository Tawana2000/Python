# Write a function to find the next higher number that can be formed using the same digits
# If it's not possible to find such a pair, indicating the input number is already in its highest possible arrangement, return the input unchanged

def nex_higher_number(num):

    digits = list(str(num))
    n = len(digits)

    i = n - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i < 0:
        return num
    
    j = n - 1
    while j > i and digits[j] <= digits[i]:
        j -= 1
    
    digits[i], digits[j] = digits[j], digits[i]


    left = i + 1
    right = n - 1
    while left < right:
        digits[left], digits[right] = digits[right], digits[left]
        left += 1
        right -= 1

    return int(''.join(digits))


print(nex_higher_number(123))
print(nex_higher_number(34532))