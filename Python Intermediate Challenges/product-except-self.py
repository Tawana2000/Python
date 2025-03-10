# Write a function to find the product of a list except for the current index

def product_except_self(nums):
    if len(nums) == 1:
        return []
    
    result, prefix, suffix = [1] * len(nums), 1, 1
    
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

print(product_except_self([5])) 
print(product_except_self([1, 2, 3, 4]))