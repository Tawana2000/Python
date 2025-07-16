# Write a function to return indices of the two numbers in an array such that they add up to a given target

def two_sum(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            

    return []

print(two_sum([6, 3, 21, 18], 24))
print(two_sum([8, 31, 16, 83, 25], 60))
print(two_sum([7, 18, 29, 43], 12))
