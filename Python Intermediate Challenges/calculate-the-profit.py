# Write a function to calculate the profit from selling a product

def calcualte_the_profit(cost_price, selling_price):

    profit = selling_price - cost_price
    return f"Profit for this product (per piece) is: {profit: g}"

cost_price = float(input("What is the cost price: "))
selling_price = float(input("What is the selling price: "))

print(calcualte_the_profit(cost_price, selling_price))
