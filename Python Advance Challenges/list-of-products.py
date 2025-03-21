# Write a function that returns a list of products from all the elements in a list excluding itself

def product_except_self(nums):

    result = []
    product = 1

    for num in nums:
        product *= num

    for num in nums:
        result.append(product // num)

    return result

print(product_except_self([1, 2, 3, 4]))