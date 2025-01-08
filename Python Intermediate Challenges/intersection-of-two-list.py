# Write a function to find the intersection of two list

def lst_intersectin(nums1, nums2):

    intersection = []
    
    for i in nums1:
        if i in nums2:
            intersection.append(i)

    return sorted(list(set(intersection)))


nums1 = list(map(int, input("Enter the first list's elements separated by space: ").split()))
nums2 = list(map(int, input("Enter the second list's element separated by space: ").split()))

print(lst_intersectin(nums1, nums2))