# Write a function to calculate the total cost of items bought for Memorial Day.

def memorial_cost(prices):
    
    return sum(int(cost) for cost in prices.split())

print(memorial_cost('20 30 40'))