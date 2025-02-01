# Write a function to find the median of two sorted lists

def find_median(nums1, nums2):
    
    result = sorted(nums1) + sorted(nums2)

    median = sum(result) / len(result)

    return median

nums1 = [1, 3]
nums2 = [2]
print(find_median(nums1, nums2))