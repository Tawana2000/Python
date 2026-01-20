#Implement binary search on a sorted list.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Test
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search(numbers, 7))   # 3
print(binary_search(numbers, 10))  # -1
