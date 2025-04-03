# Write a function to find the continguous sublist which has the largest sum
# Kadane's algorithm is used to solve this problem . It works by maintaining a current sum and an overall maximum sum. For each element in the list, it calculates the current sum by adding the element to the current sum if it is positive, or setting it to zero if it is negative. If at any point, the current sum exeeds the maximum sum, then update the maximum sum.

def max_sublist_sum(nums):

    if not nums:
        return 0
    
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

print(max_sublist_sum([-1, -5, -3, -9, 10, 25, 30]))
print(max_sublist_sum([5]))