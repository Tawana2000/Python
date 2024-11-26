# Write a fucntion to calculate the profit or loss amount of a shop

def cal_profit_loss(cost_price, selling_price):

    result = selling_price - cost_price

    if result > 0:
        return f'Profit: {result}'
    
    return f'Loss: {result * (-1)}'

cost_price = int(input('Enter the cost price: '))
selling_price = int(input('Enter the selling price: '))

print(cal_profit_loss(cost_price, selling_price))