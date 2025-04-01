# write a function to find the kth largest element in an unsorted array.

import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2)) 
