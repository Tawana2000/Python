# Write a function to find the median of two sorted arrays of different sizes.

def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    length = len(merged)
    if length % 2 == 0:
        return (merged[length // 2 - 1] + merged[length // 2]) / 2
    return merged[length // 2]

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))
