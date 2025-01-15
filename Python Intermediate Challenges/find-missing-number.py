#Write a function to find the missing number in a list of numbers

def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

print(find_missing_number([1, 2, 4, 5]))
