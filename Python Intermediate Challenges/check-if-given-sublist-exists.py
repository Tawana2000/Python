# Write a function to find if there exists a sublist in the given list with sum equal to K

def sublist_k(nums, k):
    
    current_sum, seen_sums = 0, {0}

    for num in nums:
        current_sum += num

        if current_sum - k in seen_sums:
            return True
        
        seen_sums.add(current_sum)

    return False

nums = [3, 65, 32, 2, 6, 5]
k = 35
print(sublist_k(nums, k))
        