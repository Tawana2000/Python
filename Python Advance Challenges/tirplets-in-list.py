# Write a function to find all the triplets in a list that sum to zero

def find_zero_sum_triplets(nums):
    n = len(nums)
    result = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:

                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)

    return sorted(list(result))

nums = [-1, 0, 1, 2, -1, -4]
print(find_zero_sum_triplets(nums))
